# Import the dependencies.
import numpy as np
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
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
def Welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"Precipitation: /api/v1.0/precipitation<br/>"
        f"List of Stations: /api/v1.0/stations<br/>"
        f"Temperature for one year: /api/v1.0/tobs<br/>"
        f"Start Date(yyyy-mm-dd): /api/v1.0/yyyy-mm-dd<br/>"
        f"Start Date to End Date(yyyy-mm-dd): /api/v1.0/yyyy-mm-dd/yyyy-mm-dd"
    )

@app.route('/api/v1.0/precipitation')
def Precipitation():
# Create our session (link) from Python to the DB
    session = Session(engine)
    prec = [Measurement.date,Measurement.prcp]
    result = session.query(*prec).all()
    session.close()

    total_precip = []
    for date, prcp in result:
        prcp_dict = {}
        prcp_dict["Date"] = date
        prcp_dict["Precipitation"] = prcp
        total_precip.append(prcp_dict)

    return jsonify(total_precip)


@app.route('/api/v1.0/stations')
def Stations():
    #Create session link from Python to DB
    session = Session(engine)
    """Return a list of all Stations"""
    # Query all Stations
    result = session.query(Station.station).\
                  order_by(Station.station).all()

    session.close()

    # Convert list of tuples into a normal list
    all_stations = list(np.ravel(result))

    return jsonify(all_stations)


@app.route('/api/v1.0/tobs')
def Tobs():
    # Create session from Python to the DB
    session = Session(engine)

    """Return a list of all TOBs"""
    # Query all tobs

    result = session.query(Measurement.date,Measurement.tobs,Measurement.prcp).\
                filter(Measurement.date >= '2016-08-23').\
                filter(Measurement.station=='USC00519281').\
                order_by(Measurement.date).all()
    session.close()

#Convert list to dictionary
    all_tobs = []
    for date, tobs, prcp in result:
        tobs_dict = {}
        tobs_dict["Date"] = date
        tobs_dict["Tobs"] = tobs        
        tobs_dict["Precipitation"] = prcp    
        all_tobs.append(tobs_dict)

    return jsonify(all_tobs)


@app.route("/api/v1.0/<start_date>")
def Start_date(start_date):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date"""
    # Query all tobs

    result = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start_date).all()

    session.close()

    # Create a dictionary from the row data and append to a list of start_date_tobs
    start_date_info = []
    for min, avg, max in result:
        start_date_info_dict = {}
        start_date_info_dict["Minimum Temp"] = min
        start_date_info_dict["Average Temp"] = avg
        start_date_info_dict["Maximum Temp"] = max
        start_date_info.append(start_date_info_dict) 
    return jsonify(start_date_info)


@app.route("/api/v1.0/<start_date>/<end_date>")
def Start_end_date(start_date, end_date):
    # Create session from Python to the DB
    session = Session(engine)

    """Return TMIN, TAVG, and TMAX for the dates from the start date to the end date"""
    # Query all tobs

    result = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

    session.close()
  
    # Create a dictionary from the row data and append to a list of start_end_date_tobs
    start_end_date = []
    for min, avg, max in result:
        start_end_date_dict = {}
        start_end_date_dict["Minimum Temp"] = min
        start_end_date_dict["Average Temp"] = avg
        start_end_date_dict["Maximum Temp"] = max
        start_end_date.append(start_end_date_dict) 
    

    return jsonify(start_end_date)


if __name__ == '__main__':
    app.run(debug=True)