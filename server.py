"""serves flask app and api logic for extracting fema data from csv file to
    return as usable json for rendering map"""

from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, session, jsonify
from csv_parse import parses_csv
import json
import csv

app = Flask(__name__)
app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    """Homepage."""
    return render_template('/index.html')



@app.route('/api-call')
def api_call():
    """handles logic for returning json with requested ranges of fema data"""
#For Story 1, no form input will be handled.  Return total number of incidents per state
    incidents_by_state = parses_csv()
    return jasonify(incidents_by_state)










if __name__ == "__main__":
    app.debug = True
    DebugToolbarExtension(app)
    app.run(host="0.0.0.0") 
