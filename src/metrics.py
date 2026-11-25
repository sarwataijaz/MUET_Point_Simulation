
import pandas as pd


def save_results(results):

    df = pd.DataFrame(results)

    df.to_csv(
        "results/replication_results.csv",
        index=False
    )

    metrics = [
        "completed_passengers",
        "average_waiting_time",
        "maximum_waiting_time",
        "average_queue_length",
        "maximum_queue_length",
        "bus_utilization"
    ]

    summary = df.groupby("strategy")[metrics].agg(
        ["mean", "std"]
    ).round(2)

    summary.to_csv(
        "results/scenario_comparison.csv"
    )

    print("\nFINAL SCENARIO COMPARISON")
    print(summary)
