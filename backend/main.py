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
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Application Base
app = FastAPI()

# Mount the Static File Path
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Main Application Response
@app.get("/")
async def root():
    return templates.TemplateResponse(
        "item.html",
        {"fastapi_token": "Hello World"},
    )
