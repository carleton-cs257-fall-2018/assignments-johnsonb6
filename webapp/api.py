"""
API for webapp written by Silas Monahan and Brennan Johnson
CS 257 - Jeff Ondich

"""
import sys
import flask
import json

app = flask.Flask(__name__)


@app.route('/<resort_name>/base_depth/date/<date>')
def base_depth_for_date(resort_name, date):
    """
    returns an integer that respresents base_depth for specified date
    """

@app.route('/<resort_name>/snowfall/date/<date>')
def snowfall_for_date(resort_name, date):
    """
    returns an integer that respresents snowfall for specified date
    """

@app.route('/<resort_name>/snowfall_date/year/<year>')
def highest_snowfall_for_year(resort_name, year):
    """
    returns a date that had the highest snowfall during specified year
    """
@app.route('/<resort_name>/snowfall_for_period/start_date/<start_date>/end_date/<end_date>')
def snowfall_for_period(resort_name, start_date, end_date):


@app.route('/<resort_name>/base_depth_for_period/start_date/<start_date>/end_date/<end_date>')
def base_depth_for_period(resort_name, start_date, end_date):

    
