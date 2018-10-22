"""
API for webapp written by Silas Monahan and Brennan Johnson
CS 257 - Jeff Ondich

"""
import sys
import flask
import json
import psycopg2

app = flask.Flask(__name__)
resort_table_dict = {"jackson_hole": "jackson_hole_status_reports", "snowbird": "snowbird_status_reports",
    "telluride": "telluride_status_reports", "whistler": "whistler_status_reports"}
from config import *

database = 'johnsonb6@perlman.mathcs.carleton.edu/Accounts/courses/cs257/jondich/web-f2018/johnsonb6'
user = 'johnsonb6'
password = 'Gu1t@rstring'

def get_connection():
    connection = None
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    return connection

def get_select_query_results(connection, query, parameters=None):
    '''
    Executes the specified query with the specified tuple of
    parameters. Returns a cursor for the query results.
    Raises an exception if the query fails for any reason.
    '''
    cursor = connection.cursor()
    if parameters is not None:
        cursor.execute(query, parameters)
    else:
        cursor.execute(query)
    return cursor

@app.route("/")
def default():
    return "wsup"

@app.route('/<resort_name>/base_depth/date/<date>')
def base_depth_for_date(resort_name, date):
    """
    returns an integer that respresents base_depth for specified date
    """

    resort_table = resort_table_dict[resort_name]

    query = "SELECT base_depth FROM %s WHERE status_date = CAST(%d as DATE)" %(resort_table, date)

    base_depth_list = []
    connection = get_connection()

    if connection is not None:
        try:
            for row in get_select_query_results(connection, query):
                base_depth_list.append(row)
        except Exception as e:
            print(e, file=sys.stderr)
        connection.close()
    return json.dumps(base_depth_list)

@app.route('/<resort_name>/snowfall/date/<date>')
def snowfall_for_date(resort_name, date):
    """
    returns an integer that respresents snowfall for specified date
    """

    resort_table = resort_table_dict[resort_name]

    query = "SELECT snowfall FROM %s WHERE status_date = CAST(%d as DATE)" %(resort_table, date)
    connection = get_connection()

    snowfall_list = []

    if connection is not None:
        try:
            for row in get_select_query_results(connection, query):
                snowfall_list.append(row)
        except Exception as e:
            print(e, file=sys.stderr)
        connection.close()
    return json.dumps(snowfall_list)

@app.route('/<resort_name>/snowfall_date/year/<year>')
def highest_snowfall_for_year(resort_name, year):
    """
    returns a date that had the highest snowfall during specified year
    """
    resort_table = resort_table_dict[resort_name]

    query = "SELECT snowfall FROM %s WHERE (EXTRACT(YEAR FROM TIMESTAMP status_date) = %d)" %(resort_table, year)
    connection = get_connection()

    snowfall_list = []

    if connection is not None:
        try:
            for row in get_select_query_results(connection, query):
                snowfall_list.append(row)
        except Exception as e:
            print(e, file=sys.stderr)
        connection.close()
    snowfall_list.sort(reverse=True)
    """
    need to think about making our own sorter so we can break ties effectively
    """
    highest_snowfall = snowfall_list[0]
    return json.dumps(highest_snowfall)

@app.route('/<resort_name>/snowfall_for_period/start_date/<start_date>/end_date/<end_date>')
def snowfall_for_period(resort_name, start_date, end_date):
    """
    returns list of snowfall for each date in the period
    """
    #ddmmyyyy
    start_date_parts = start_date.split("-")
    start_date_year = int(start_date_parts[2])
    start_date_month = int(start_date_parts[1])
    start_date_day = int(start_date_parts[0])

    end_date_parts = end_date.split("-")
    end_date_year = int(end_date_parts[2])
    end_date_month = int(end_date_parts[1])
    end_date_day = int(end_date_parts[0])

    resort_table = resort_table_dict[resort_name]

    query = "SELECT status_date FROM %s" %(resort_table)
    connection = get_connection()

    period_date_list = []
    snowfall_list = []

    if connection is not None:
        try:
            for row in get_select_query_results(connection, query):
                row_parts = row.split("-")
                #yyyymmdd
                row_year = int(row_parts[0])
                row_month = int(row_parts[1])
                row_day = int(row_parts[2])

                if row_year < start_date_year and row_year > end_date_year:
                    continue
                if start_date_year == row_year:
                    if start_date_month > row_month:
                        continue
                if start_date_year == row_year:
                    if start_date_month == row_month:
                        if start_date_day > row_day:
                            continue
                if end_date_year == row_year:
                    if end_date_month < row_month:
                        continue
                if end_date_year == row_year:
                    if end_date_month == row_month:
                        if end_date_day < row_day:
                            continue

                period_date_list.append(row)
        except Exception as e:
            print(e, file=sys.stderr)


    refined_query = "SELECT snowfall FROM %s WHERE (status_date in period_date_list)" %(resort_table)
    if connection is not None:
        try:
            for row in get_select_query_results(connection, refined_query):
                snowfall_list.append(row)
        except Exception as e:
            print(e, file=sys.stderr)




    return json.dumps(snowfall_list)

@app.route('/<resort_name>/base_depth_for_period/start_date/<start_date>/end_date/<end_date>')
def base_depth_for_period(resort_name, start_date, end_date):
    """
    returns list of base_depth for each date in the period
    """
    #ddmmyyyy
    start_date_parts = start_date.split("-")
    start_date_year = int(start_date_parts[2])
    start_date_month = int(start_date_parts[1])
    start_date_day = int(start_date_parts[0])

    end_date_parts = end_date.split("-")
    end_date_year = int(end_date_parts[2])
    end_date_month = int(end_date_parts[1])
    end_date_day = int(end_date_parts[0])

    resort_table = resort_table_dict[resort_name]

    query = "SELECT status_date FROM %s" %(resort_table)
    connection = get_connection()

    period_date_list = []
    base_depth_list = []

    if connection is not None:
        try:
            for row in get_select_query_results(connection, query):
                row_parts = row.split("-")
                #yyyymmdd
                row_year = int(row_parts[0])
                row_month = int(row_parts[1])
                row_day = int(row_parts[2])

                if row_year < start_date_year and row_year > end_date_year:
                    continue
                if start_date_year == row_year:
                    if start_date_month > row_month:
                        continue
                if start_date_year == row_year:
                    if start_date_month == row_month:
                        if start_date_day > row_day:
                            continue
                if end_date_year == row_year:
                    if end_date_month < row_month:
                        continue
                if end_date_year == row_year:
                    if end_date_month == row_month:
                        if end_date_day < row_day:
                            continue

                period_date_list.append(row)
        except Exception as e:
            print(e, file=sys.stderr)


    refined_query = "SELECT base_depth FROM %s WHERE (status_date in period_date_list)" %(resort_table)
    if connection is not None:
        try:
            for row in get_select_query_results(connection, refined_query):
                base_depth_list.append(row)
        except Exception as e:
            print(e, file=sys.stderr)




    return json.dumps(base_depth_list)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]))
        print('  Example: {0} perlman.mathcs.carleton.edu 5101'.format(sys.argv[0]))
        exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    app.run(host=host, port=port, debug=True)
