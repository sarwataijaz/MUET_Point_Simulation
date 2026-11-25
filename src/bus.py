
"""
Bus model for MUET Point Bus Simulation.
"""


class Bus:

    def __init__(self, bus_id, capacity, terminal=None):

        self.bus_id = bus_id

        self.capacity = capacity

        self.terminal = terminal

        self.passengers = []

        self.is_available = True

        self.total_passengers_transported = 0

        self.total_busy_time = 0

        self.last_departure_time = None

    @property
    def passenger_count(self):

        return len(self.passengers)

    @property
    def available_seats(self):

        return self.capacity - self.passenger_count

    def board_passenger(self, passenger, current_time):

        if self.passenger_count >= self.capacity:
            return False

        passenger.board(current_time)

        self.passengers.append(passenger)

        return True

    def depart(self):

        boarded_passengers = self.passengers.copy()

        self.total_passengers_transported += len(
            boarded_passengers
        )

        self.passengers.clear()

        return boarded_passengers

    def __repr__(self):

        return (
            f"Bus(id={self.bus_id}, "
            f"capacity={self.capacity}, "
            f"passengers={self.passenger_count}, "
            f"available={self.is_available})"
        )
