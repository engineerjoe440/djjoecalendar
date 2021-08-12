################################################################################
"""
DJ JOE Website Availability Calendar
------------------------------------

(c) 2021 - Stanley Solutions - Joe Stanley

This application serves the React frontend required to demonstrate the available
dates for DJ Joe Services.
"""
################################################################################

import datetime
import os.path
from date_support import daterange, _clean_dates, _restore_datetimes
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def google_calendar_service_available():
    """Quickly Determines if Token is Available for Google Calendar System."""
    return os.path.exists('token.json')

def get_google_datetime(google_dt_dict):
    """Performs dictionary-specific handling to attempt extraction of dt."""
    google_dt = google_dt_dict.get('dateTime', google_dt_dict.get('date'))
    return google_dt.split("T")[0]

def get_service():
    """Gets a handle to the Google Calendar Service."""
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if google_calendar_service_available():
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    return service

def googlify_datetimes(dts):
    dts = _restore_datetimes(_clean_dates(dts))
    return [dt.isoformat()+"Z" for dt in dts]

def get_event_list(start: datetime.datetime, end: datetime.datetime):
    """Identifies a list of all events in the specified date range."""
    service = get_service()

    start, end = googlify_datetimes([start, end])

    # Call the Calendar API
    events_result = service.events().list(calendarId='primary', timeMin=start,
                                          timeMax=end, singleEvents=True,
                                          orderBy='startTime').execute()
    return events_result.get('items', [])

def get_occupied_dates(start: datetime.datetime, end: datetime.datetime):
    """Generates a list of single dt objects representing occupied dates."""
    if not google_calendar_service_available():
        return [] # Bail Out without Attempting Connection
    events = get_event_list(start=start, end=end)
    occupied_dates = []

    # Iteratively process each event
    for event in events:
        start_date = datetime.datetime.strptime(
            get_google_datetime(event['start']),
            "%Y-%m-%d",
        )
        end = event.get('end')
        if end != None:
            end_date = get_google_datetime(end)
            if end_date != None:
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
    now = datetime.datetime.now()
    events = get_event_list(now, now + datetime.timedelta(days=30))
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
    
    print(get_occupied_dates(now, now + datetime.timedelta(days=30)))