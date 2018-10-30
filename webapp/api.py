
"""
API for webapp written by Silas Monahan and Brennan Johnson
CS 257 - Jeff Ondich

"""
import sys
import flask
import json
import psycopg2
app = flask.Flask(__name__, static_folder = 'static', template_folder = 'templates')
resort_table_dict = {"jackson_hole": "jackson_hole_status_reports", "snowbird": "snowbird_status_reports",
    "telluride": "telluride_status_reports", "whistler": "whistler_status_reports"}


database_for_use = 'johnsonb6'
user_name = 'johnsonb6'
password_name = 'Gu1t@rstring'

def get_connection():
    connection = None
    try:
        connection = psycopg2.connect(database=database_for_use, user=user_name, password=password_name)
    except Exception as e:
        print(e, file=sys.stderr)
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


@app.route("/<resort_name>/base_depth/date/<date>")
def base_depth_for_date(resort_name, date):
    """
    returns an integer that respresents base_depth for specified date
    """

    resort_table = resort_table_dict[resort_name]

    new_date = str(date)
    base_depth_to_return = None
    query = "SELECT base_depth FROM %s WHERE status_date = to_date(%s::text, 'YYYYMMDD')" %(resort_table, date)

    connection = get_connection()

    if connection is not None:
        try:
            for row in get_select_query_results(connection, query):
                base_depth_to_return = row
        except Exception as e:
            print(e, file=sys.stderr)
        connection.close()
    return json.dumps(base_depth_to_return)
@app.route("/<resort_name>/base_depth_average/date/<date>")
def base_depth_average_for_date(resort_name, date):
    """
    returns average of base depth across all years on specific date
    """

    resort_table = resort_table_dict[resort_name]

    date_month = int(date[4:6])
    date_day = int(date[6:8])
    query = "SELECT base_depth FROM %s WHERE CAST(EXTRACT(MONTH FROM status_date) AS INTEGER) = %d AND CAST(EXTRACT(DAY FROM status_date) AS INTEGER) = %d" %(resort_table, date_month, date_day)
    connection = get_connection()
    total = 0
    counter = 0
    for row in get_select_query_results(connection, query):
        counter += 1
        total += int(row[0])
    base_depth_to_return = int(total/counter)
    return json.dumps(base_depth_to_return)


@app.route('/<resort_name>/snowfall/date/<date>')
def snowfall_for_date(resort_name, date):
    """
    returns an integer that respresents snowfall for specified date
    """

    resort_table = resort_table_dict[resort_name]

    new_date = str(date)

    query = "SELECT snowfall FROM %s WHERE status_date = to_date(%s::text, 'YYYYMMDD')" %(resort_table, new_date)
    connection = get_connection()
    snowfall_to_return = None


    if connection is not None:
        try:
            for row in get_select_query_results(connection, query):
                snowfall_to_return = row
        except Exception as e:
            print(e, file=sys.stderr)

        connection.close()
    return json.dumps(snowfall_to_return)

@app.route('/<resort_name>/snowfall_date/year/<year>')
def highest_snowfall_for_year(resort_name, year):
    """
    returns a date that had the highest snowfall during specified year
    """
    resort_table = resort_table_dict[resort_name]
    year = int(year)
    query = "SELECT snowfall FROM %s WHERE CAST(EXTRACT(YEAR FROM status_date) AS INTEGER) = %d" %(resort_table, year)
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

    #yyyymmdd
    start_date_year = int(start_date[0:4])
    start_date_month = int(start_date[4:6])
    start_date_day = int(start_date[6:8])

    end_date_year = int(end_date[0:4])
    end_date_month = int(end_date[4:6])
    end_date_day = int(end_date[6:8])

    resort_table = resort_table_dict[resort_name]

    query = "SELECT status_date FROM %s" %(resort_table)
    connection = get_connection()

    period_date_list = []
    snowfall_list = []

    if connection is not None:
        try:
            for row in get_select_query_results(connection, query):
                #yyyymmdd
                row_year = int(row[0].strftime('%Y'))
                row_month = int(row[0].strftime('%m'))
                row_day = int(row[0].strftime('%d'))

                if row_year < start_date_year or row_year > end_date_year:
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
                date_to_append = (row[0].strftime('%Y') + row[0].strftime('%m') + row[0].strftime('%d'))
                period_date_list.append(date_to_append)

        except Exception as e:
            print(e, file=sys.stderr)

    for date in period_date_list:
        snowfall_to_add = snowfall_for_date(resort_name, date)
        snowfall_list.append(snowfall_to_add)

    return json.dumps(snowfall_list)

@app.route('/<resort_name>/base_depth_for_period/start_date/<start_date>/end_date/<end_date>')
def base_depth_for_period(resort_name, start_date, end_date):
    """
    returns list of base_depth for each date in the period
    """

    start_date_year = int(start_date[0:4])
    start_date_month = int(start_date[4:6])
    start_date_day = int(start_date[6:8])

    end_date_year = int(end_date[0:4])
    end_date_month = int(end_date[4:6])
    end_date_day = int(end_date[6:8])

    resort_table = resort_table_dict[resort_name]

    query = "SELECT status_date FROM %s" %(resort_table)
    connection = get_connection()

    period_date_list = []
    base_depth_list = []

    if connection is not None:
        try:
            for row in get_select_query_results(connection, query):
                row_year = int(row[0].strftime('%Y'))
                row_month = int(row[0].strftime('%m'))
                row_day = int(row[0].strftime('%d'))

                if row_year < start_date_year or row_year > end_date_year:
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

                date_to_add = (row[0].strftime('%Y') + row[0].strftime('%m') + row[0].strftime('%d'))
                period_date_list.append(date_to_add)

        except Exception as e:
            print(e, file=sys.stderr)

    for date in period_date_list:
        base_depth_for_list = base_depth_for_date(resort_name, date)
        base_depth_list.append(base_depth_for_list)

    return json.dumps(base_depth_list)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]))
        print('  Example: {0} perlman.mathcs.carleton.edu 5101'.format(sys.argv[0]))
        exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    app.run(host=host, port=port, debug=True)
