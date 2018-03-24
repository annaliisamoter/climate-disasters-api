"""serves flask app and api logic for extracting fema data from csv file to
    return as usable json for rendering map"""

from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, jsonify
from csv_parse import parses_csv


app = Flask(__name__, static_folder='static', static_url_path='')
app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""
    return render_template('/index.html')


@app.route('/api-call')
def api_call():
    """handles logic for returning json with requested filtering ranges of fema data"""

    inputs = request.args
    print("these are the unparsed inputs: ", inputs)
    begin_range = inputs['begin']
    end_range = inputs['end']
    disaster_type = inputs['type-of-disaster']
    print("These are the begin_range, end_range and disaster_type", begin_range, end_range, disaster_type)
    
    incidents_by_state = parses_csv(begin_range, end_range, disaster_type)
    print("api call is being made")
    print(incidents_by_state)
    

    return jsonify(incidents_by_state)










if __name__ == "__main__":
    app.debug = True
    #DebugToolbarExtension(app)
    app.run(host="0.0.0.0", port=5005)
