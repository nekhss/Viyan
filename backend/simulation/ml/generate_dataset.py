from pathlib import Path
import math
import random

import pandas as pd

NUM_SAMPLES = 50000

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = BASE_DIR / "collision_dataset.csv"


def generate_sample():

    # Most conjunctions are relatively far apart.
    distance = round(random.triangular(0.01, 20.0, 12.0), 3)

    # Relative velocity clusters around realistic orbital values.
    relative_velocity = round(
        max(0.5, min(random.gauss(7.5, 2.0), 15.0)),
        3,
    )

    # Altitude differences usually aren't extreme.
    altitude_difference = round(
        abs(random.gauss(20.0, 15.0)),
        3,
    )

    # Most encounters happen with several minutes of notice.
    time_to_closest = int(
        random.triangular(60, 3600, 1200)
    )

    # Priority difference is skewed toward smaller values.
    priority_difference = random.choices(
        population=range(11),
        weights=[
            30, 20, 15, 10, 8,
            6, 4, 3, 2, 1, 1
        ],
        k=1
    )[0]

    score = 0.0

    # Distance (largest contributor)
    if distance < 0.5:
        score += 5
    elif distance < 2:
        score += 4
    elif distance < 5:
        score += 2

    # Relative velocity
    if relative_velocity > 11:
        score += 2
    elif relative_velocity > 8:
        score += 1

    # Altitude difference
    if altitude_difference < 3:
        score += 2
    elif altitude_difference < 10:
        score += 1

    # Time to closest approach
    if time_to_closest < 180:
        score += 2
    elif time_to_closest < 600:
        score += 1

    # Mission priority
    score += priority_difference * 0.15

    # Convert score into probability.
    probability = 1 / (1 + math.exp(-(score - 5)))

    # Environmental uncertainty.
    probability += random.uniform(-0.08, 0.08)

    probability = max(0.0, min(1.0, probability))

    collision = (
        1
        if random.random() < probability
        else 0
    )

    return [
        distance,
        relative_velocity,
        altitude_difference,
        time_to_closest,
        priority_difference,
        collision,
    ]


def main():

    dataset = [
        generate_sample()
        for _ in range(NUM_SAMPLES)
    ]

    df = pd.DataFrame(
        dataset,
        columns=[
            "closest_distance_km",
            "relative_velocity_km_s",
            "altitude_difference_km",
            "time_to_closest_sec",
            "priority_difference",
            "collision_risk",
        ],
    )

    df.to_csv(OUTPUT_FILE, index=False)

    print(df.head())

    print("\nDataset Statistics")
    print(df.describe())

    print(
        "\nCollision Distribution:"
    )
    print(
        df["collision_risk"]
        .value_counts(normalize=True)
        .rename("ratio")
    )

    print(
        f"\nGenerated {len(df)} samples."
    )

    print(
        f"Saved to:\n{OUTPUT_FILE}"
    )


if __name__ == "__main__":
    main()