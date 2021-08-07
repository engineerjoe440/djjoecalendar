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


class DatePeriod(BaseModel):
    start_year: str
    start_month: str
    start_day: str
    end_year: str
    end_month: str
    end_day: str

# Application Base
app = FastAPI()

# Mount the Static File Path
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

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
    with open("./foo.txt", 'w') as f:
        f.write(str(dates.__dict__))
    return {
        "events": [],
    }
