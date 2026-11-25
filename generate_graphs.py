
import os
import pandas as pd
import matplotlib.pyplot as plt

# Load simulation results
df = pd.read_csv("results/replication_results.csv")

# Calculate mean and standard deviation for each strategy
summary = df.groupby("strategy").agg({
    "average_waiting_time": ["mean", "std"],
    "average_queue_length": ["mean", "std"],
    "completed_passengers": ["mean", "std"],
    "bus_utilization": ["mean", "std"]
})

# Create output directory
os.makedirs("graphs", exist_ok=True)

# Graph configurations
graph_configs = [
    {
        "metric": "average_waiting_time",
        "title": "Average Passenger Waiting Time",
        "ylabel": "Waiting Time (minutes)",
        "filename": "average_waiting_time.png"
    },
    {
        "metric": "average_queue_length",
        "title": "Average Passenger Queue Length",
        "ylabel": "Number of Passengers",
        "filename": "average_queue_length.png"
    },
    {
        "metric": "completed_passengers",
        "title": "Average Completed Passengers",
        "ylabel": "Number of Passengers",
        "filename": "completed_passengers.png"
    },
    {
        "metric": "bus_utilization",
        "title": "Average Bus Fleet Utilization",
        "ylabel": "Utilization (%)",
        "filename": "bus_utilization.png"
    }
]

strategies = ["baseline", "improved", "optimized"]

# Generate individual graphs
for config in graph_configs:

    metric = config["metric"]

    means = [
        summary.loc[strategy, (metric, "mean")]
        for strategy in strategies
    ]

    stds = [
        summary.loc[strategy, (metric, "std")]
        for strategy in strategies
    ]

    plt.figure(figsize=(8, 5))

    plt.bar(
        strategies,
        means,
        yerr=stds,
        capsize=6
    )

    plt.title(config["title"])
    plt.xlabel("Scheduling Strategy")
    plt.ylabel(config["ylabel"])
    plt.grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()

    plt.savefig(
        f"graphs/{config['filename']}",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print(f"Generated: graphs/{config['filename']}")

print("\nAll four graphs generated successfully!")
