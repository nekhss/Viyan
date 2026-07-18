import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "satellite_telemetry.json"


def load_telemetry():
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def get_satellite(name: str):
    satellites = load_telemetry()

    for satellite in satellites:
        if (
            satellite["id"].lower() == name.lower()
            or satellite["name"].lower() == name.lower()
        ):
            return satellite

    return None