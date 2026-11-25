# MUET Point Bus Scheduling and Queue Management Simulation

A Python-based Discrete Event Simulation (DES) project developed using **SimPy** to analyze passenger queues, bus scheduling strategies, waiting times, and fleet utilization in the MUET Point bus transportation system.

## Project Overview

The MUET Point bus system serves students, faculty, and staff travelling between different locations, including STC and Main Gate. During peak hours, passenger demand can create long queues, extended waiting times, and inefficient use of available buses.

This project models a simplified MUET Point transportation system and evaluates three scheduling strategies to investigate how dispatching decisions affect passenger service and fleet performance.

The objective is to identify a scheduling approach that reduces passenger waiting time and queue length while improving fleet utilization, without increasing the number of buses.

## Objectives

- Model passenger arrivals and queues at multiple terminals.
- Simulate a shared fleet of buses with limited passenger capacity.
- Implement and compare three bus dispatching strategies.
- Measure passenger waiting time, queue length, passenger throughput, and bus utilization.
- Evaluate the performance of alternative scheduling policies through repeated simulation experiments.

## Technologies Used

- **Python** – Main programming language
- **SimPy** – Discrete Event Simulation framework
- **NumPy** – Numerical calculations
- **Pandas** – Experimental data processing and CSV generation
- **Matplotlib** – Visualization and graph generation

## System Configuration

The simulation uses the following assumed input parameters:

| Parameter | Value |
|---|---:|
| Simulation duration | 90 minutes |
| Total buses | 6 |
| Passenger capacity per bus | 40 |
| Terminals | STC, Main Gate |
| STC passenger arrival rate | 0.8 passengers/minute |
| Main Gate passenger arrival rate | 0.6 passengers/minute |
| Nominal one-way travel time | 20 minutes |
| Boarding time per passenger | 2 seconds |
| Baseline dispatch interval | 15 minutes |
| Improved dispatch interval | 10 minutes |
| Optimized dispatch threshold | 8 passengers |
| Number of replications | 30 |

**Note:** These values are simulation assumptions used to demonstrate and compare scheduling strategies. They should not be interpreted as verified operational statistics of MUET Point.

## Scheduling Strategies

### 1. Baseline Strategy

Uses a fixed bus dispatch interval of 15 minutes. When the scheduled dispatch time is reached, an available bus is assigned to a terminal with passengers waiting.

### 2. Improved Fixed-Interval Strategy

Uses a shorter fixed dispatch interval of 10 minutes. This strategy investigates whether more frequent dispatching can improve passenger service and fleet performance.

### 3. Optimized Demand-Based Strategy

Uses a queue-based dispatch policy. A bus is dispatched when a terminal's passenger queue reaches the configured threshold of 8 passengers. When multiple terminals meet the threshold, the terminal with the larger queue is selected.

## Simulation Methodology

The system uses Discrete Event Simulation to represent passenger arrivals, queue formation, bus dispatching, passenger boarding, and bus travel.

Passenger arrivals are generated using exponentially distributed interarrival times, corresponding to a Poisson arrival process with the configured terminal-specific arrival rates.

Each bus has a limited seating capacity. After boarding passengers, the bus travels to complete its outbound journey and subsequently returns to become available for another dispatch.

A centralized fleet is shared between the two terminals. Each simulation replication uses a random seed, and the three strategies are evaluated using the same replication seed to maintain comparable passenger demand patterns.

The simulation is repeated 30 times for each strategy to account for randomness in passenger arrivals and travel times.

## Performance Metrics

The following metrics are used to evaluate the scheduling strategies:

- **Completed Passengers:** Number of passengers who complete their outbound bus journey within the simulation period.
- **Average Waiting Time:** Average time passengers spend waiting before boarding.
- **Maximum Waiting Time:** Longest passenger waiting time observed in an individual replication.
- **Average Queue Length:** Average sampled number of passengers waiting across the terminals.
- **Maximum Queue Length:** Highest sampled queue length observed in an individual replication.
- **Bus Utilization:** Percentage of available fleet time spent on boarding and travel activities.

The reported comparison uses the mean and standard deviation of each metric across 30 replications.

## Experimental Results

The following table presents the mean results across 30 simulation replications. Standard deviations are shown in parentheses.

| Metric | Baseline | Improved | Optimized |
|---|---:|---:|---:|
| Completed Passengers | 81.63 (12.46) | 90.57 (13.42) | 89.83 (13.05) |
| Average Waiting Time (min) | 7.76 (0.60) | 7.89 (1.07) | 6.27 (0.61) |
| Mean Maximum Waiting Time (min) | 17.03 (4.98) | 28.25 (6.14) | 21.92 (3.48) |
| Average Queue Length | 5.84 (0.69) | 5.73 (0.88) | 4.70 (0.64) |
| Mean Maximum Queue Length | 17.27 (1.84) | 20.27 (4.36) | 15.43 (3.49) |
| Bus Utilization (%) | 60.14 (2.13) | 70.70 (1.84) | 69.99 (4.85) |

### Key Findings

- The optimized strategy achieved the lowest average passenger waiting time, approximately 6.27 minutes.
- It also achieved the lowest average queue length, approximately 4.70 passengers.
- Compared with the baseline strategy, optimized scheduling reduced average waiting time by approximately 19.2%.
- Bus utilization increased from 60.14% under baseline scheduling to 69.99% under optimized scheduling.
- The improved fixed-interval strategy achieved the highest average passenger throughput, but did not achieve the lowest average waiting time.

Overall, the optimized strategy provided the best balance between passenger waiting time, queue management, and fleet utilization, although it did not outperform every strategy on every metric.

## Project Structure

```text
MUET_Point_Simulation/
│
├── src/
│   ├── config.py
│   ├── passenger.py
│   ├── bus.py
│   ├── terminal.py
│   ├── scheduler.py
│   ├── simulation.py
│   └── metrics.py
│
├── experiments/
├── results/
│   ├── replication_results.csv
│   └── scenario_comparison.csv
│
├── graphs/
│   ├── average_waiting_time.png
│   ├── average_queue_length.png
│   ├── completed_passengers.png
│   └── bus_utilization.png
│
├── tests/
├── main.py
├── generate_graphs.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Execution

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/MUET_Point_Simulation.git
cd MUET_Point_Simulation
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the simulation

```bash
python main.py
```

This executes 30 replications for all three scheduling strategies and generates:

- `results/replication_results.csv`
- `results/scenario_comparison.csv`

### 5. Generate graphs

```bash
python generate_graphs.py
```

The four comparison graphs are saved in the `graphs/` directory.

## Limitations

- Passenger arrival rates and operational parameters are assumed rather than collected from official MUET Point records.
- The simulation represents a simplified two-terminal transportation system.
- The model uses a fixed nominal travel-time range and does not incorporate live traffic information.
- The demand-based scheduling policy uses a fixed queue threshold rather than a continuously learning optimization algorithm.
- The simulation does not represent every operational constraint, such as route-specific schedules, vehicle breakdowns, or real-time passenger destinations.

## Future Improvements

- Collect actual passenger arrival and bus operation data.
- Incorporate time-dependent passenger demand.
- Introduce maximum-waiting-time-based dispatch rules.
- Explore optimization algorithms for fleet allocation.
- Extend the model to additional terminals and routes.
- Incorporate traffic-dependent travel-time predictions.

## Conclusion

This project demonstrates how Discrete Event Simulation can be used to analyze passenger queues and evaluate alternative bus scheduling policies. The experimental results indicate that demand-based dispatching can reduce average passenger waiting time and queue length while improving fleet utilization under the modeled assumptions.

The project provides a foundation for further investigation into more efficient and responsive MUET Point transportation scheduling.

---

**Course:** Simulation and Modelling  
**Department:** Software Engineering  
**University:** Mehran University of Engineering and Technology (MUET), Jamshoro

**Developed as an academic Problem-Based Learning (PBL) project.**