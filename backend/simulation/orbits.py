"""
Orbit propagation using SGP4.
"""

from sgp4.api import Satrec
from skyfield.api import load, EarthSatellite

ts = load.timescale()


def load_satellite(tle):
    return Satrec.twoline2rv(
        tle["line1"],
        tle["line2"]
    )


def current_position(tle):

    satellite = EarthSatellite(
        tle["line1"],
        tle["line2"],
        tle["name"],
        ts
    )

    t = ts.now()

    geocentric = satellite.at(t)

    x, y, z = geocentric.position.km

    return {
        "name": tle["name"].strip(),
        "x": float(x),
        "y": float(y),
        "z": float(z)
    }


if __name__ == "__main__":

    from data_loader import fetch_tle, parse_tle

    tle_text = fetch_tle()
    satellites = parse_tle(tle_text)

    for sat in satellites[:5]:
        print(current_position(sat))
        