"""
data_loader.py

Loads TLE data from CelesTrak with automatic caching.
"""

import os
import time
import requests

# ------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------

CACHE_DIR = os.path.join(os.path.dirname(__file__), "data")
CACHE_EXPIRY = 2 * 60 * 60  # 2 hours

CELESTRAK_URL = (
    "https://celestrak.org/NORAD/elements/"
    "gp.php?GROUP={group}&FORMAT=tle"
)


# ------------------------------------------------------------------
# Download / Cache
# ------------------------------------------------------------------

def fetch_tle(group="starlink", force_refresh=False):
    """
    Fetch TLE data for the given satellite group.

    Parameters
    ----------
    group : str
        Example: starlink, stations, oneweb, planet, active
    force_refresh : bool
        Ignore cache and download again.

    Returns
    -------
    str
        Raw TLE text.
    """

    os.makedirs(CACHE_DIR, exist_ok=True)

    cache_file = os.path.join(CACHE_DIR, f"{group}.tle")

    # ---------------------------
    # Load cached file
    # ---------------------------

    if os.path.exists(cache_file) and not force_refresh:

        age = time.time() - os.path.getmtime(cache_file)

        if age < CACHE_EXPIRY:
            print(f"[CACHE] Using cached {group} dataset")

            with open(cache_file, "r", encoding="utf-8") as f:
                return f.read()

    # ---------------------------
    # Download fresh data
    # ---------------------------

    print(f"[DOWNLOAD] Fetching {group} dataset...")

    response = requests.get(
        CELESTRAK_URL.format(group=group),
        timeout=20
    )

    response.raise_for_status()

    with open(cache_file, "w", encoding="utf-8") as f:
        f.write(response.text)

    print(f"[CACHE] Saved to {cache_file}")

    return response.text


# ------------------------------------------------------------------
# Parse TLE
# ------------------------------------------------------------------

def parse_tle(tle_text):
    """
    Convert raw TLE text into a list of satellites.
    """

    lines = [ line.strip() for line in tle_text.splitlines() if line.strip()]

    satellites = []

    for i in range(0, len(lines), 3):

        if i + 2 >= len(lines):
            break

        satellites.append({
            "name": lines[i].strip(),
            "line1": lines[i + 1].strip(),
            "line2": lines[i + 2].strip()
        })

    return satellites


# ------------------------------------------------------------------
# Public API
# ------------------------------------------------------------------

def load_satellites(group="starlink", force_refresh=False):
    """
    Fetch and parse satellites.

    Returns
    -------
    list[dict]
    """

    tle_text = fetch_tle(
        group=group,
        force_refresh=True
    )

    return parse_tle(tle_text)


# ------------------------------------------------------------------
# Test
# ------------------------------------------------------------------

if __name__ == "__main__":

    satellites = load_satellites(group="starlink")

    print(f"\nLoaded {len(satellites)} satellites\n")

    for sat in satellites[:5]:
        print(sat["name"])