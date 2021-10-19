################################################################################
"""
DJ JOE Website Availability Calendar
------------------------------------

(c) 2021 - Stanley Solutions - Joe Stanley

This application serves the React frontend required to demonstrate the available
dates for DJ Joe Services.
"""
################################################################################

# Requirements
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from datetime import datetime
from date_support import weekends_in_range, remove_excluded_dates
from google_calendar import get_occupied_dates


class DatePeriod(BaseModel):
    start: datetime
    end: datetime

# Application Base
app = FastAPI()

# Mount the Static File Path
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Available Date List Generator
def generate_available_dates(dates: DatePeriod):
    print(dates.start, dates.end)
    # Identify Available Date Information
    included_dates = weekends_in_range(start=dates.start, end=dates.end)
    excluded_dates = get_occupied_dates(start=dates.start, end=dates.end)
    # Remove Days That are Busy
    days_avail = remove_excluded_dates(
        inclusive_dates=included_dates,
        exclude_dates=excluded_dates,
    )
    available = []
    # Iteratively Build Structure for JSON
    for date in days_avail:
        available.append({
            'title': "Available!",
            'start': date,
            'end': date,
            'allDay': True,
            'resource': '',
        })
    return available

# Main Application Response
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "fastapi_token": "Hello World"
        },
    )

# Main API Endpoint to Serve Available Dates
@app.post("/api/getavailability")
async def availability(dates: DatePeriod):
    return {"events": generate_available_dates(dates=dates)}
