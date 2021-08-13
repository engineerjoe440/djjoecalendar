################################################################################
"""
DJ JOE Website Availability Calendar
------------------------------------

(c) 2021 - Stanley Solutions - Joe Stanley

This application serves the React frontend required to demonstrate the available
dates for DJ Joe Services.
"""
################################################################################

from datetime import timedelta, datetime

def daterange(date1, date2):
    """Iterator over a range of days specified between the two dates."""
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

def weekends_in_range(start, end):
    """Generate a list of the weekend days in the range specified."""
    weekdays = [0,1,2,3,4] # 0 is Monday
    weekend_days = []
    today = datetime(*datetime.today().timetuple()[:3], tzinfo=start.tzinfo)
    # Determine Month of Interest
    if (start.day > 1) and (end.month > start.month + 1):
        start = datetime(start.year, start.month+1, 1, tzinfo=start.tzinfo)
    for dt in daterange(start, end):
        if dt.month > start.month:
            break
        if dt.weekday() not in weekdays and dt > today:
            weekend_days.append(dt)
    return weekend_days

def _clean_dates(datetimes):
    for i, date in enumerate(datetimes):
        datetimes[i] = date.date()
    return datetimes

def _restore_datetimes(dates):
    for i, date in enumerate(dates):
        dates[i] = datetime.combine(date, datetime.min.time())
    return dates

def remove_excluded_dates(inclusive_dates, exclude_dates):
    """Identify a list of days that are "available" for bookings."""
    inclusive_dates = _clean_dates(inclusive_dates)
    exclude_dates = _clean_dates(exclude_dates)
    return _restore_datetimes(list(set(inclusive_dates) - set(exclude_dates)))

if __name__ == "__main__":
    included = weekends_in_range(
        datetime(2020, 5, 1),
        datetime(2020, 5, 30),
    )
    excluded = weekends_in_range(
        datetime(2020, 5, 1),
        datetime(2020, 5, 11),
    )
    print(remove_excluded_dates(included, excluded))