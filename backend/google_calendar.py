################################################################################
"""
DJ JOE Website Availability Calendar
------------------------------------

(c) 2021 - Stanley Solutions - Joe Stanley

This application serves the React frontend required to demonstrate the available
dates for DJ Joe Services.
"""
################################################################################

# Import Requisites
import os
import datetime
import requests
from date_support import daterange, _clean_dates, _restore_datetimes

ENV_API_KEY = "GOOGLE_API_KEY"

BASE_URL = (
    "https://clients6.google.com/calendar/v3/calendars/engineerjoe440@gmail.com"
    "/events?calendarId=engineerjoe440%40gmail.com&singleEvents=true&timeZone="
    "America%2FLos_Angeles&maxAttendees=1&maxResults=250&sanitizeHtml=true&"
    "timeMin={TIME_MIN}&timeMax={TIME_MAX}&key={API_KEY}"
)

################################################################################
# Supporting Functions

def googlify_datetimes(dts):
    dts = _restore_datetimes(_clean_dates(dts))
    return [dt.isoformat()+"Z" for dt in dts]

def get_google_date(google_dt_dict):
    """Performs dictionary-specific handling to attempt extraction of dt."""
    google_dt = google_dt_dict.get('dateTime', google_dt_dict.get('date'))
    return google_dt.split("T")[0]

def get_google_time(google_dt_dict):
    """Performs dictionary-specific handling to attempt extraction of dt."""
    google_dt = google_dt_dict.get('dateTime', google_dt_dict.get('date'))
    try:
        timestring = google_dt.split("T")[1].split('-')[0]
    except IndexError:
        timestring = "00:00:00"
    return timestring

################################################################################
# Event Listing Functions

def get_event_list(start: datetime.datetime, end: datetime.datetime):
    """Identifies a list of all events in the specified date range."""
    start, end = googlify_datetimes([start, end])

    # Call the Calendar API
    REQ_URL = BASE_URL.format(
        TIME_MIN = start,
        TIME_MAX = end,
        API_KEY = os.getenv(ENV_API_KEY),
    )
    print(REQ_URL)
    resp = requests.get(REQ_URL)
    if resp.status_code == 200:
        return resp.json().get('items', [])
    else:
        print(
            "GOOGLE REQUEST FAILED:",
            resp.status_code,
            resp.reason,
        )
        return []

def get_occupied_dates(start: datetime.datetime, end: datetime.datetime):
    """Generates a list of single dt objects representing occupied dates."""
    events = get_event_list(start=start, end=end)
    occupied_dates = []

    # Iteratively process each event
    for event in events:
        start_date = datetime.datetime.strptime(
            get_google_date(event['start']),
            "%Y-%m-%d",
        )
        end = event.get('end')
        if end != None:
            end_date = get_google_date(end)
            end_time = datetime.datetime.strptime(get_google_time(end), "%H:%M:%S")
            if end_date != None and end_time.hour != 0:
                end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
                for date in daterange(start_date, end_date):
                    # Append all dates in range
                    occupied_dates.append(date)
            else:
                # Append only start date
                occupied_dates.append(start_date)
        else:
            # Append only start date
            occupied_dates.append(start_date)
    
    return occupied_dates


if __name__ == '__main__':
    now = datetime.datetime.now() - datetime.timedelta(days=20)
    events = get_event_list(now, now + datetime.timedelta(days=30))
    for event in events:
        print(event['start'].get('dateTime', event['start'].get('date')))
    if len(events) == 0:
        print("NO EVENTS FOUND")
    events = get_occupied_dates(now, now + datetime.timedelta(days=30))
    for event in events:
        print("event", event)
    if len(events) == 0:
        print("NO EVENTS FOUND")