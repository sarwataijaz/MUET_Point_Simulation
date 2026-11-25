
"""
Terminal queue management for MUET Point Simulation.
"""

from collections import deque


class Terminal:

    def __init__(self, name):

        self.name = name
        self.queue = deque()
        self.total_arrivals = 0
        self.total_boarded = 0
        self.queue_history = []

    def add_passenger(self, passenger):

        self.queue.append(passenger)
        self.total_arrivals += 1

    def board_passengers(self, bus, current_time):

        boarded = []

        while self.queue and bus.available_seats > 0:

            passenger = self.queue[0]

            if bus.board_passenger(passenger, current_time):

                self.queue.popleft()
                boarded.append(passenger)
                self.total_boarded += 1

        return boarded

    def record_queue_length(self, current_time):

        self.queue_history.append({
            "time": current_time,
            "queue_length": len(self.queue)
        })
