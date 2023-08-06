# sqlalchemy-challenge

## Background

### Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

## Part 1: Analyze and Explore the Climate Data

### Project work began by using Python and SQLAlchemy to do a basic climate analysis and data exploration of the supplied climate database. Instructions were to use SQLAlchemy ORM queries, Pandas, and Matplotlib.  

1. Precipitation analysis included determining the most recent date in the given dataset and gathering the prior 12 months of precipitation data through queries.  The query results were put into a dataframe and the datafram plot method was used to plot the results. Finishing the analysis by printing out the summary statistics for the precipitation data using Pandas.

2. Station analysis 

  A. Started with running a query to calculate the total number of weather stations.  
  B. Second query was created to determine the most active weather stations.  
  C. Third query was created to produce the TMIN, TAVG, and TMAX TOBS (time of observation bias)of the most active weather station
  determined in the second query.
  D. Final query collect the prior 12 months of temperature observation (TOBS) data. The results were then p0lotted as a histogram with bins=12.

## Part 2: Design Your Climate App

### The challenge was to design a Flask API based on the queries that were developed in Part 1.

### 5 Routes in the Flask API (app.py)

1. Homepage - Lists all the available routes.
2. Precipitation - Precipitation analysis results for the last 12 months of data
3. Stations - The list of all weather stations
4. TOBS (Time of Observation Bias - The query results for most active weather station (date and temp observations) for last year.
5. Start Date - For a specified start date, calculations of TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
6. Start-End Date - For a specified start date and end date, calculations of TMIN, TAVG, and TMAX for the dates from the start date to the end date

The Flask jsonify function was used to convert the API data to a valid JSON response object.

### File Names/Folder Names

SurfsUp folder containing: app.py (Flask API app/code), climate_starter.ipynb (Jupyter notebook and python code), data folder (Resources) containing the 2 csv data files and sqlite db file, Readme.md file.
