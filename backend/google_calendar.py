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
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def google_calendar_service_available():
    """Quickly Determines if Token is Available for Google Calendar System."""
    return os.path.exists('token.json')

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

def get_event_list(start: datetime.datetime, end: datetime.datetime):
    """Identifies a list of all events in the specified date range."""
    service = get_service()

    start = start.isoformat() + 'Z' # 'Z' indicates UTC time
    end = end.isoformat() + 'Z'

    # Call the Calendar API
    events_result = service.events().list(calendarId='primary', timeMin=start,
                                          timeMax=end, singleEvents=True,
                                          orderBy='startTime').execute()
    return events_result.get('items', [])



if __name__ == '__main__':
    now = datetime.datetime.now()
    events = get_event_list(now, now + datetime.timedelta(days=30))
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])