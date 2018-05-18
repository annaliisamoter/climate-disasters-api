"""serves simple flask app and api logic for extracting fema data from csv file to
    return as usable json."""

from flask import Flask, render_template, request, jsonify
from csv_parse import parses_csv


app = Flask(__name__, static_folder='static', static_url_path='')
app.secret_key = "ABC"


@app.route('/')
def index():
    """Homepage."""
    return render_template('/index.html')


@app.route('/api-call')
def api_call():
    """handles logic for returning json with requested filtering ranges of fema data"""

    inputs = request.args
    begin_range = inputs['begin']
    end_range = inputs['end']
    disaster_type = inputs['type-of-disaster'] 
    incidents_by_state = parses_csv(begin_range, end_range, disaster_type)
    return jsonify(incidents_by_state)


if __name__ == "__main__":
    app.debug = False
    TEMPLATES_AUTO_RELOAD = True
    app.run(host="0.0.0.0", port=5005)
