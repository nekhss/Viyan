"""
Known spacecraft relationships that should not
trigger collision warnings.
"""

DOCKED_PAIRS = {

    tuple(sorted(("ISS (ZARYA)", "POISK"))),

    tuple(sorted(("ISS (ZARYA)", "ISS (NAUKA)"))),

    tuple(sorted(("ISS (ZARYA)", "CREW DRAGON 12"))),

    tuple(sorted(("ISS (ZARYA)", "PROGRESS-MS 33"))),

    tuple(sorted(("ISS (ZARYA)", "CYGNUS NG-24"))),

    tuple(sorted(("CSS (TIANHE)", "CSS (WENTIAN"))),

    tuple(sorted(("CSS (TIANHE)", "CSS (MENGTIAN"))),

    tuple(sorted(("CSS (TIANHE)", "TIANZHOU-10"))),

    tuple(sorted(("CSS (TIANHE)", "SHENZHOU-23 (SZ-23)"))),

}

def is_expected_proximity(name1, name2):
    """
    Return True if the pair represents
    docked or permanently associated spacecraft.
    """

    pair = tuple(sorted((name1, name2)))

    return pair in DOCKED_PAIRS