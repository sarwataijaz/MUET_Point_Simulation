
from src.simulation import MUETSimulation
from src.metrics import save_results


def main():

    strategies = [
        "baseline",
        "improved",
        "optimized"
    ]

    results = []

    REPLICATIONS = 30

    for seed in range(1, REPLICATIONS + 1):

        print(f"\nReplication {seed}/{REPLICATIONS}")

        for strategy in strategies:

            simulation = MUETSimulation(
                strategy,
                seed=seed
            )

            result = simulation.run()

            result["replication"] = seed

            results.append(result)

            print(
                f"{strategy}: "
                f"{result['completed_passengers']} completed"
            )

    save_results(results)


if __name__ == "__main__":
    main()
