
"""
Configuration settings for MUET Point Bus Simulation.
"""

# -------------------------------
# Simulation Configuration
# -------------------------------

SIMULATION_DURATION = 90  # minutes

RANDOM_SEED = 42

# -------------------------------
# Transportation Terminals
# -------------------------------

TERMINALS = [
    "STC",
    "Main Gate"
]

# -------------------------------
# Bus Fleet Configuration
# -------------------------------

TOTAL_BUSES = 6

BUS_CAPACITY = 40

# Time required for one-way travel (minutes)
TRAVEL_TIME = 20

# -------------------------------
# Passenger Arrival Configuration
# -------------------------------

# Initial synthetic arrival rates.
# These are experimental assumptions, not actual MUET statistics.

PASSENGER_ARRIVAL_RATES = {
    "STC": 0.8,
    "Main Gate": 0.6
}

# -------------------------------
# Boarding Configuration
# -------------------------------

BOARDING_TIME_PER_PASSENGER = 2 / 60  # minutes

# -------------------------------
# Scheduling Configuration
# -------------------------------

BASELINE_DEPARTURE_INTERVAL = 15  # minutes

IMPROVED_DEPARTURE_INTERVAL = 10  # minutes

# Dynamic dispatch threshold
QUEUE_DISPATCH_THRESHOLD = 20
