# import the necessary packages
from flask import Flask
import json
import os

app = Flask(__name__)

from ha_api import routes
