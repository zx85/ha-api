# import the necessary packages
from flask import render_template, url_for, flash, redirect, request
from ha_api import app
import os
import json
import datetime
import time
from include.google_sheets import Spreadsheet
from include.logger import log

def local_time_now():
    now=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    log.debug(f"in local_time_now function - now is {now}")
    return now

def make_date_list(hour=False):
    date_list=[]
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    updated_timstm = local_time_now()
    if hour:
        date_string=date_string = f'{year:02d}-{month:02d}-{day:02d} {hour:02d}:00'
        date_list=[year,month,day,hour, date_string, updated_timstm]
    else:
        date_string=date_string = f'{year:02d}-{month:02d}-{day:02d}'
        date_list=[year,month,day,date_string, updated_timstm]
    return date_list

# Initialize spreadsheet
def init_sheet(sheet_name):
    sheet = Spreadsheet(
    creds_file=f"/app/google.json",
    spreadsheet_name="Solar Database"
    )
    active_sheet=sheet.spreadsheet.worksheet(sheet_name)
    return active_sheet

# boggo immersion stuff
@app.route("/api/immersion", methods=["GET"])
def immersion():
    secret = request.args.get("secret", "")
    if secret == "b1533944bfbf7a4d":
        hour = request.args.get("hour", int(datetime.datetime.now().hour))
        minutes = int(request.args.get("minutes", "30"))
        if minutes > 0:
            response = "inserted data"
            row_fields=make_date_list()
            row_fields.extend([hour,minutes])
            sheet=init_sheet("immersion")
            sheet.append_row(row_fields)
        else:
            response = "0 minutes - ignored"
        return response
    else:
        return "You got it wrong.", 401


# bonus powerups stuff - very similar to immersion really.
@app.route("/api/powerups", methods=["GET"])
def powerups():
    secret = request.args.get("secret", "")
    if secret == "b1533944bfbf7a4d":
        hour = request.args.get("hour", datetime.datetime.now().hour)
        row_fields=make_date_list()
        row_fields.append(hour)
        log.debug(f"row_fields is: {row_fields}")
        sheet=init_sheet("powerups")
        sheet.append_row(row_fields)
        return "inserted data"
    else:
        return "You got it wrong.", 401


# Day forecast stuff
@app.route("/api/solarForecastDay", methods=["GET"])
def sfd():
    secret = request.args.get("secret", "")
    if secret == "b1533944bfbf7a4d":      
        solar_gen = float(request.args.get("solarGen", 0))
        row_fields=make_date_list()
        row_fields.append(solar_gen)
        sheet=init_sheet("solarForecastDay")
        sheet.append_row(row_fields)
        response = "inserted data for solaarForecastDay"

        return response
    else:
        return "You got it wrong.", 401


# Hour forecast stuff
@app.route("/api/solarForecastHour", methods=["GET"])
def sfh():
    secret = request.args.get("secret", "")
    if secret == "b1533944bfbf7a4d":

        hour = int(request.args.get("hour", str((datetime.datetime.now().hour) + 1)))
        solar_gen = float(request.args.get("solarGen", 0))

        if float(solar_gen) > 0:
            row_fields=make_date_list(hour)
            row_fields.append(solar_gen)
            sheet=init_sheet("solarForecastHour")
            sheet.append_row(row_fields)
            response = "inserted data for solarForecastHour"

        else:
            response = "Value is zero so not bothering to add to solarForecastHour"
        return response
    else:
        return "You got it wrong.", 401
