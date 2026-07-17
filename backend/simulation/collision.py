"""
Future conjunction detection.
"""

import math
from simulation.trajectory import predict_trajectory

CONJUNCTION_THRESHOLD_KM = 5.0


def euclidean(pos1, pos2):
    """
    Euclidean distance between two positions.
    """

    return math.sqrt(
        (pos1["x"] - pos2["x"]) ** 2 +
        (pos1["y"] - pos2["y"]) ** 2 +
        (pos1["z"] - pos2["z"]) ** 2
    )


def closest_approach(traj1, traj2):
    """
    Returns the closest encounter between two trajectories.
    """

    minimum = float("inf")
    best = None

    for point1, point2 in zip(traj1, traj2):

        distance = euclidean(
            point1["position"],
            point2["position"]
        )

        if distance < minimum:

            minimum = distance

            best = {
                "distance": distance,
                "time_offset": point1["time_offset"],
                "state1": point1,
                "state2": point2
            }

    return best


def detect_future_conjunctions(
    tles,
    threshold=CONJUNCTION_THRESHOLD_KM,
    prediction_minutes=30,
    step_seconds=60,
):
    """
    Detect all future conjunctions.
    """

    trajectories = {}

    for tle in tles:

        trajectories[tle["name"]] = predict_trajectory(
            tle,
            minutes=prediction_minutes,
            step=step_seconds
        )
        print(f"{tle['name']}: {len(trajectories[tle['name']])} points")
    conjunctions = []

    for i in range(len(tles)):

        for j in range(i + 1, len(tles)):

            sat1 = tles[i]
            sat2 = tles[j]

            closest = closest_approach(
                trajectories[sat1["name"]],
                trajectories[sat2["name"]]
            )
            if closest is None:
                continue
            if closest["distance"] <= threshold:

                conjunctions.append({

                    "satellite1": {
                        "name": sat1["name"].strip(),
                        "position": closest["state1"]["position"],
                        "velocity": closest["state1"]["velocity"]
                    },

                    "satellite2": {
                        "name": sat2["name"].strip(),
                        "position": closest["state2"]["position"],
                        "velocity": closest["state2"]["velocity"]
                    },

                    "closest_distance_km": round(
                        closest["distance"], 3
                    ),

                    "time_to_closest_sec":
                        closest["time_offset"]

                })

    return conjunctions