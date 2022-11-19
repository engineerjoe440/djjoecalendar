################################################################################
"""
DJ JOE Website Availability Calendar
------------------------------------

(c) 2022 - Stanley Solutions - Joe Stanley

This application serves the React frontend required to demonstrate the available
dates for DJ Joe Services.
"""
################################################################################

import sys
from datetime import datetime
from pathlib import Path

BACKEND_ROOT = Path(__file__).parent.parent / Path("backend")

sys.path.insert(0, BACKEND_ROOT)

from date_support import weekends_in_range

def test_verify_excluded():
    included = weekends_in_range(
        datetime(2021, 12, 26),
        datetime(2022, 2, 5),
    )
    excluded = weekends_in_range(
        datetime(2022, 1, 15),
        datetime(2022, 1, 16),
    )
    print(remove_excluded_dates(included, excluded))

def test_verify_excluded_2():
    included = weekends_in_range(
        datetime(2022, 11, 27),
        datetime(2022, 12, 31),
    )
    excluded = [datetime(2022, 12, 10)]
    print(remove_excluded_dates(included, excluded))