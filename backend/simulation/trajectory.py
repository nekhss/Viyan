from datetime import datetime, timedelta, timezone

from skyfield.api import load, EarthSatellite,wgs84

ts = load.timescale()


def predict_trajectory(tle, minutes=30, step=60):
    """
    Predict satellite trajectory for the next `minutes`.

    Returns position and velocity at each timestep.
    """

    satellite = EarthSatellite(
        tle["line1"],
        tle["line2"],
        tle["name"],
        ts
    )

    start = datetime.now(timezone.utc)

    trajectory = []

    for sec in range(0, minutes * 60 + 1, step):

        t = ts.from_datetime(start + timedelta(seconds=sec))

        state = satellite.at(t)

        # Position (km)
        x, y, z = state.position.km

        # Velocity (km/s)
        vx, vy, vz = state.velocity.km_per_s

        subpoint = wgs84.subpoint(state)

        latitude = float(subpoint.latitude.degrees)
        longitude = float(subpoint.longitude.degrees)
        altitude = float(subpoint.elevation.km)

        trajectory.append({

            "time_offset": sec,

            "position": {
                "x": float(x),
                "y": float(y),
                "z": float(z)
            },

            "velocity": {
                "vx": float(vx),
                "vy": float(vy),
                "vz": float(vz)
            },

            "geographic": {
            "latitude": latitude,
            "longitude": longitude,
           "altitude_km": altitude
            }

        })

    return trajectory