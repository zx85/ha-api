# import the necessary packages
from flask import render_template, url_for, flash, redirect, request
from ha_api import app, dbInfo
import os
import json
import datetime


# boggo immersion stuff
@app.route("/api/immersion", methods=["GET"])
def immersion():
    secret = request.args.get("secret", "")
    if secret == "b1533944bfbf7a4d":
        hour = request.args.get("hour", str(datetime.datetime.now().hour))
        minutes = request.args.get("minutes", "30")
        year = str(datetime.datetime.now().year)
        month = str(datetime.datetime.now().month)
        day = str(datetime.datetime.now().day)
        if int(minutes) > 0:
            response = "inserted data"

        # TODO: Add functionality for adding to Google Sheets

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
        hour = request.args.get("hour", str(datetime.datetime.now().hour))
        year = str(datetime.datetime.now().year)
        month = str(datetime.datetime.now().month)
        day = str(datetime.datetime.now().day)
        response = "inserted data"

        # TODO: Add functionality for adding to Google Sheets

        return response
    else:
        return "You got it wrong.", 401


# Day forecast stuff
@app.route("/api/solarForecastDay", methods=["GET"])
def sfd():
    secret = request.args.get("secret", "")
    if secret == "b1533944bfbf7a4d":
        year = str(datetime.datetime.now().year)
        month = str(datetime.datetime.now().month)
        day = str(datetime.datetime.now().day)
        solarGen = request.args.get("solarGen", 0)

        response = "inserted data for solaarForecastDay"

        # TODO: Add functionality for adding to Google Sheets

        return response
    else:
        return "You got it wrong.", 401


# Hour forecast stuff
@app.route("/api/solarForecastHour", methods=["GET"])
def sfh():
    secret = request.args.get("secret", "")
    if secret == "b1533944bfbf7a4d":
        hour = request.args.get("hour", str((datetime.datetime.now().hour) + 1))
        year = str(datetime.datetime.now().year)
        month = str(datetime.datetime.now().month)
        day = str(datetime.datetime.now().day)
        solarGen = request.args.get("solarGen", 0)

        if float(solarGen) > 0:
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
