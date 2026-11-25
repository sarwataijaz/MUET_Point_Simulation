
"""
Passenger model for MUET Point Bus Simulation.
"""


class Passenger:
    """
    Represents an individual passenger in the transportation system.
    """

    def __init__(self, passenger_id, terminal, arrival_time):

        self.passenger_id = passenger_id

        self.terminal = terminal

        self.arrival_time = arrival_time

        self.boarding_time = None

        self.departure_time = None

        self.waiting_time = None

        self.is_boarded = False

    def board(self, current_time):
        """
        Record the time when the passenger boards a bus.
        """

        self.boarding_time = current_time

        self.waiting_time = (
            self.boarding_time - self.arrival_time
        )

        self.is_boarded = True

    def depart(self, current_time):
        """
        Record the time when the passenger reaches their destination.
        """

        self.departure_time = current_time

    def __repr__(self):

        return (
            f"Passenger(id={self.passenger_id}, "
            f"terminal={self.terminal}, "
            f"arrival={self.arrival_time:.2f})"
        )

