from typing import Dict
import numpy as np


FEATURE_COLUMNS = [
    "closest_distance_km",
    "relative_velocity_km_s",
    "altitude_difference_km",
    "time_to_closest_sec",
    "priority_difference",
]


def prepare_features(features: Dict) -> np.ndarray:
    """
    Convert simulation features into a machine-learning feature vector.
    """

    encounter = features["encounter"]

    sat1 = features["satellite1"]
    sat2 = features["satellite2"]

    priority_difference = abs(
        sat1["priority"] -
        sat2["priority"]
    )

    vector = np.array([
        encounter["closest_distance_km"],
        encounter["relative_velocity_km_s"],
        encounter["altitude_difference_km"],
        encounter["time_to_closest_sec"],
        priority_difference
    ], dtype=float)

    return vector.reshape(1, -1)