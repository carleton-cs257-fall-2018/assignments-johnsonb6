#!/usr/bin/env python3
'''
    psycopg2-sample.py
    Jeff Ondich, 23 April 2016
    A very short demo of how to use psycopg2 to connect to and
    query a PostgreSQL database. This demo assumes a "books"
    database like the one I've used in CS257 Spring 2016, including
    an authors table with fields (id, first_name, last_name,...).
    You might also want to consult the official psycopg2 tutorial
    at https://wiki.postgresql.org/wiki/Psycopg2_Tutorial.
'''
import psycopg2

# Storing your user name and password directly in your code
# is easiest:
#
#   database = 'yourdatabasename'
#   user = 'yourusername'
#   password = 'yourdatabasepassword'
#
# However, this introduces potential security problems, which we'll
# discuss in class. One common mitigation of these dangers is to put
# the data in a separate module that's in the Python import path,
# but not in the web server's file tree.
from config import password
from config import database
from config import user
database = 'johnsonb6@perlman.mathcs.carleton.edu/Accounts/courses/cs257/jondich/web-f2018/johnsonb6'
user = 'johnsonb6'
password = 'Gu1t@rstring'
# Connect to the database
try:
    connection = psycopg2.connect(database=database, user=user, password=password)
except Exception as e:
    print(e)
    exit()

try:
    cursor = connection.cursor()
    query = "SELECT base_depth FROM jackson_hole_status_reports WHERE status_date = CAST(2009-12-31 as DATE)"
    cursor.execute(query)
except Exception as e:
    print(e)
    exit()


print("base depth on dec 31 2009 in jackson hole")
for row in cursor:
    print(row)
print(" ")




connection.close()
