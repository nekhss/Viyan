"""
Feature extraction for conjunction events.
"""

import math

from simulation.satellite_registry import get_satellite_metadata

EARTH_RADIUS_KM = 6371.0


def magnitude(vector):
    """
    Returns magnitude of a 3D vector.
    """

    return math.sqrt(
        vector["vx"] ** 2 +
        vector["vy"] ** 2 +
        vector["vz"] ** 2
    )


def altitude(position):
    """
    Compute altitude above Earth's surface.
    """

    distance = math.sqrt(
        position["x"] ** 2 +
        position["y"] ** 2 +
        position["z"] ** 2
    )

    return distance - EARTH_RADIUS_KM


def relative_velocity(v1, v2):
    """
    Relative velocity between satellites.
    """

    return math.sqrt(

        (v1["vx"] - v2["vx"]) ** 2 +

        (v1["vy"] - v2["vy"]) ** 2 +

        (v1["vz"] - v2["vz"]) ** 2

    )


def extract_features(conjunction):
    """
    Convert a conjunction event into a feature vector.
    """

    sat1 = conjunction["satellite1"]
    sat2 = conjunction["satellite2"]

    meta1 = get_satellite_metadata(sat1["name"])
    meta2 = get_satellite_metadata(sat2["name"])

    altitude1 = altitude(sat1["position"])
    altitude2 = altitude(sat2["position"])

    rel_vel = relative_velocity(
        sat1["velocity"],
        sat2["velocity"]
    )

    return {

        "satellite1": {

            "name": sat1["name"],

            "operator": meta1["operator"],

            "mission": meta1["mission"],

            "priority": meta1["priority"],

            "position": sat1["position"],

            "velocity": sat1["velocity"],

            "speed_km_s": round(
                magnitude(sat1["velocity"]),
                3
            ),

            "altitude_km": round(
                altitude1,
                3
            )

        },

        "satellite2": {

            "name": sat2["name"],

            "operator": meta2["operator"],

            "mission": meta2["mission"],

            "priority": meta2["priority"],

            "position": sat2["position"],

            "velocity": sat2["velocity"],

            "speed_km_s": round(
                magnitude(sat2["velocity"]),
                3
            ),

            "altitude_km": round(
                altitude2,
                3
            )

        },

        "encounter": {

            "closest_distance_km":
                conjunction["closest_distance_km"],

            "time_to_closest_sec":
                conjunction["time_to_closest_sec"],

            "relative_velocity_km_s":
                round(rel_vel, 6),

            "altitude_difference_km":
                round(abs(altitude1 - altitude2), 3)

        }

    }