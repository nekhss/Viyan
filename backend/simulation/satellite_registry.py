"""
Satellite metadata registry.

Maps satellite names to operator, mission type and priority.
"""

SATELLITE_REGISTRY = {

    "STARLINK": {
        "operator": "SpaceX",
        "mission": "Communication",
        "priority": 4
    },

    "ONEWEB": {
        "operator": "OneWeb",
        "mission": "Communication",
        "priority": 5
    },

    "ISS": {
        "operator": "NASA / Roscosmos",
        "mission": "Human Spaceflight",
        "priority": 10
    },

    "CSS": {
        "operator": "CNSA",
        "mission": "Human Spaceflight",
        "priority": 10
    },

    "SENTINEL": {
        "operator": "ESA",
        "mission": "Earth Observation",
        "priority": 9
    },

    "LANDSAT": {
        "operator": "NASA / USGS",
        "mission": "Earth Observation",
        "priority": 9
    },

    "NOAA": {
        "operator": "NOAA",
        "mission": "Weather",
        "priority": 8
    },

    "TERRA": {
        "operator": "NASA",
        "mission": "Earth Observation",
        "priority": 9
    },

    "AQUA": {
        "operator": "NASA",
        "mission": "Earth Observation",
        "priority": 9
    }

}


DEFAULT_METADATA = {

    "operator": "Unknown",

    "mission": "Unknown",

    "priority": 5

}


def get_satellite_metadata(name):
    """
    Returns metadata for a satellite based on its name.
    """

    upper_name = name.upper()

    for key, value in SATELLITE_REGISTRY.items():

        if key in upper_name:
            return value

    return DEFAULT_METADATA