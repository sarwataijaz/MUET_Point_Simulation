
"""Centralized shared-fleet MUET Point simulation."""

import simpy
import random
import numpy as np

from src.config import *
from src.passenger import Passenger
from src.bus import Bus
from src.terminal import Terminal
from src.scheduler import Scheduler


class MUETSimulation:

    def __init__(self, strategy, seed=RANDOM_SEED):

        self.env = simpy.Environment()
        self.strategy = strategy

        # Separate random generators ensure identical
        # passenger arrivals across scheduling strategies.
        self.arrival_rng = random.Random(seed)
        self.traffic_rng = random.Random(seed + 100)

        self.terminals = {
            name: Terminal(name) for name in TERMINALS
        }

        self.buses = [
            Bus(i + 1, BUS_CAPACITY)
            for i in range(TOTAL_BUSES)
        ]

        self.scheduler = Scheduler(strategy)

        self.passenger_id = 0
        self.waiting_times = []
        self.completed_passengers = 0
        self.bus_log = []
        self.busy_time = 0

    def passenger_generator(self, terminal_name, rate):

        terminal = self.terminals[terminal_name]

        while True:

            delay = self.arrival_rng.expovariate(rate)

            yield self.env.timeout(delay)

            self.passenger_id += 1

            passenger = Passenger(
                self.passenger_id,
                terminal_name,
                self.env.now
            )

            terminal.add_passenger(passenger)

    def dispatch_bus(self, bus, terminal):

        bus.is_available = False

        self.env.process(
            self.bus_trip(bus, terminal)
        )

    def bus_trip(self, bus, terminal):

        boarded = terminal.board_passengers(
            bus, self.env.now
        )

        if not boarded:
            bus.is_available = True
            return

        self.waiting_times.extend(
            passenger.waiting_time
            for passenger in boarded
        )

        # Boarding duration
        boarding_duration = (
            len(boarded) * BOARDING_TIME_PER_PASSENGER
        )

        self.busy_time += min(
            boarding_duration,
            max(0, SIMULATION_DURATION - self.env.now)
        )

        yield self.env.timeout(boarding_duration)

        passengers = bus.depart()

        self.bus_log.append({
            "time": self.env.now,
            "bus_id": bus.bus_id,
            "terminal": terminal.name,
            "passengers": len(passengers)
        })

        # Outbound journey
        outbound = self.traffic_rng.uniform(
            TRAVEL_TIME * 0.8,
            TRAVEL_TIME * 1.2
        )

        self.busy_time += min(
            outbound,
            max(0, SIMULATION_DURATION - self.env.now)
        )

        yield self.env.timeout(outbound)

        for passenger in passengers:
            passenger.depart(self.env.now)

        self.completed_passengers += len(passengers)

        # Return journey before the bus becomes available
        return_time = self.traffic_rng.uniform(
            TRAVEL_TIME * 0.8,
            TRAVEL_TIME * 1.2
        )

        self.busy_time += min(
            return_time,
            max(0, SIMULATION_DURATION - self.env.now)
        )

        yield self.env.timeout(return_time)

        bus.is_available = True

    def dispatcher(self):

        while True:

            yield self.env.timeout(1)

            candidates = self.scheduler.get_dispatch_candidates(
                self.env.now,
                self.terminals
            )

            for terminal in candidates:

                available_buses = [
                    bus for bus in self.buses
                    if bus.is_available
                ]

                if not available_buses:
                    break

                bus = available_buses[0]

                self.dispatch_bus(bus, terminal)

            for terminal in self.terminals.values():
                terminal.record_queue_length(self.env.now)

    def run(self):

        for terminal_name, rate in PASSENGER_ARRIVAL_RATES.items():

            self.env.process(
                self.passenger_generator(
                    terminal_name, rate
                )
            )

        self.env.process(self.dispatcher())

        self.env.run(until=SIMULATION_DURATION)

        return self.get_results()

    def get_results(self):

        total_remaining = (
            self.passenger_id - self.completed_passengers
        )

        queue_lengths = [
            record["queue_length"]
            for terminal in self.terminals.values()
            for record in terminal.queue_history
        ]

        return {
            "strategy": self.strategy,
            "total_arrivals": self.passenger_id,
            "completed_passengers": self.completed_passengers,
            "remaining_passengers": total_remaining,

            "average_waiting_time": (
                np.mean(self.waiting_times)
                if self.waiting_times else 0
            ),

            "maximum_waiting_time": (
                np.max(self.waiting_times)
                if self.waiting_times else 0
            ),

            "average_queue_length": (
                np.mean(queue_lengths)
                if queue_lengths else 0
            ),

            "maximum_queue_length": (
                max(queue_lengths)
                if queue_lengths else 0
            ),

            "bus_utilization": (
                self.busy_time /
                (TOTAL_BUSES * SIMULATION_DURATION) * 100
            )
        }
