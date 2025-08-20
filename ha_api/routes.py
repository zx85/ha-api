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

# Initialize spreadsheet
sheet = Spreadsheet(
creds_file=f"/app/google.json",
spreadsheet_name="Solar Database"
)
immersion_sheet=sheet.spreadsheet.worksheet("immersion")
powerups_sheet=sheet.spreadsheet.worksheet("powerups")
solar_forecast_day_sheet=sheet.spreadsheet.worksheet("solarForecastDay")
solar_forecast_hour_sheet=sheet.spreadsheet.worksheet("solarForecastHour")

# boggo immersion stuff
@app.route("/api/immersion", methods=["GET"])
def immersion():
    secret = request.args.get("secret", "")
    if secret == "b1533944bfbf7a4d":
        hour = request.args.get("hour", int(datetime.datetime.now().hour))
        minutes = int(request.args.get("minutes", "30"))
        year = f'{datetime.datetime.now().year:02d}'
        month = f'{datetime.datetime.now().month:02d}'
        day = f'{datetime.datetime.now().day:02d}'
        date_string = f'{year}-{month}-{day}'
        updated_timstm = local_time_now()
        if int(minutes) > 0:
            response = "inserted data"
            row_fields=[year, month, day, date_string, updated_timstm, hour, minutes]
            immersion_sheet.append_row(row_fields)
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
        hour = request.args.get("hour", int(datetime.datetime.now().hour))
        year = f'{datetime.datetime.now().year:02d}'
        month = f'{datetime.datetime.now().month:02d}'
        day = f'{datetime.datetime.now().day:02d}'
        date_string = f'{year}-{month}-{day}'
        updated_timstm = local_time_now()

        row_fields=[year, month, day, date_string, updated_timstm, hour]
        powerups_sheet.append_row(row_fields)
        return "inserted data"
    else:
        return "You got it wrong.", 401


# Day forecast stuff
@app.route("/api/solarForecastDay", methods=["GET"])
def sfd():
    secret = request.args.get("secret", "")
    if secret == "b1533944bfbf7a4d":
        year = f'{datetime.datetime.now().year:02d}'
        month = f'{datetime.datetime.now().month:02d}'
        day = f'{datetime.datetime.now().day:02d}'
        date_string = f'{year}-{month}-{day}'
        updated_timstm = local_time_now()
        solar_gen = float(request.args.get("solarGen", 0))

        row_fields=[year, month, day, date_string, updated_timstm, solar_gen]
        solar_forecast_day_sheet.append_row(row_fields)
        response = "inserted data for solaarForecastDay"

        return response
    else:
        return "You got it wrong.", 401


# Hour forecast stuff
@app.route("/api/solarForecastHour", methods=["GET"])
def sfh():
    secret = request.args.get("secret", "")
    if secret == "b1533944bfbf7a4d":
        year = f'{datetime.datetime.now().year:02d}'
        month = f'{datetime.datetime.now().month:02d}'
        day = f'{datetime.datetime.now().day:02d}'
        hour = request.args.get("hour", str((datetime.datetime.now().hour) + 1))
        date_string = f'{year}-{month}-{day} {hour}:00'
        updated_timstm = local_time_now()
        solar_gen = float(request.args.get("solarGen", 0))

        if float(solar_gen) > 0:
            row_fields=[year, month, day, hour, date_string, updated_timstm, solar_gen]
            solar_forecast_hour_sheet.append_row(row_fields)
            response = "inserted data for solarForecastHour"
            # cnx = mysql.connector.connect(user=dbInfo['dbuser'],
            # password=dbInfo['dbpass'],
            # host=dbInfo['dbhost'], port=dbInfo['dbport'],
            # database=dbInfo['dbname'], auth_plugin='mysql_native_password')
            # cur=cnx.cursor()
            # cur.execute("insert into solarForecastHour (year,month,day,hour,solarGen) values ("+year+","+month+","+day+","+hour+","+solarGen+")")
            # cnx.commit()
            # cur.close()
        else:
            response = "Value is zero so not bothering to add to solarForecastHour"
        return response
    else:
        return "You got it wrong.", 401
