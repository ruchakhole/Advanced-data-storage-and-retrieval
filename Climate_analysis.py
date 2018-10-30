import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to the measurement and station tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Avalable Routes:<br/>"
        f"/api/v1.0/precipitation - Precipitation values for last year<br/>"

        f"/api/v1.0/stations - List of stations<br/>"

        f"/api/v1.0/tobs - List of temperature observations for previous year<br/>"

        f"/api/v1.0/&ltstart&gt - List of minimum, average and maximum temperatures for a given <start> date in yyyy-mm-dd format to now<br/>"

        f"/api/v1.0/&ltstart&gt/&ltend&gt - List of minimum, average and maximum temperatures for a given <start> date in yyyy-mm-dd format to a given <end> date in yyyy-mm-dd format<br/>"
    )

