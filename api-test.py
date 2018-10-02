#!/usr/bin/env python3
'''
    api-test.py
    Alexis Engel, Brennan Johnson, and Silas Monahan


'''

import sys
import argparse
import json
import urllib.request


def get_top_movies():
	# gives you a list of top movies
	base_url = 'https://api.themoviedb.org/3/movie/popular?api_key=89036379e923b4f7b34eaa4b513982e5'
	url = base_url.format(movies)

	data_from_server = urllib.request.urlopen(url).read()
	string_from_server = data_from_server.decode('utf-8')
	top_movies = json.loads(string_from_server)

	return top_movies


def movies_in_theater():
	# returns a list of movies in theaters
	base_url = 'https://api.themoviedb.org/discover/movie?primary_release_date.gte=2014-09-15&primary_release_date.lte=2014-10-22'
	#url = base_url.format(movies)

	data_from_server = urllib.request.urlopen(base_url).read()
	string_from_server = data_from_server.decode('utf-8')
	theater_movies = json.loads(string_from_server)

	return theater_movies


def get_budget_for_movie(movie_id):


	base_url = 'https://api.themoviedb.org/3/movie/24?api_key=89036379e923b4f7b34eaa4b513982e5&language=en-US'
	#url = base_url.format()

	data_from_server = urllib.request.urlopen(base_url).read()
	string_from_server = data_from_server.decode('utf-8')
	movie_name = json.loads(string_from_server)["title"]
	movie_budget = json.loads(string_from_server)["budget"]

	return movie_name, movie_budget

"""
def main(args):
    if args.action == 'movies_in_theater':
        print(movies_in_theater())
    elif args.action == 'get top movies':
        print(get_top_movies())
"""


if __name__ == '__main__':

    api_key = '89036379e923b4f7b34eaa4b513982e5'
    """
    parser = argparse.ArgumentParser(description='Get movie info from the IMDB API')
    parser.add_argument('action', metavar = 'action', help = "usage: 'movies in theater' or 'get top movies'", choices = ["movies_in_theater", "get top movies"])
    args = parser.parse_args()
    main(args)
    """
    i = int(sys.argv[1])
    print(i)
    movie_id = i
    print(get_budget_for_movie(movie_id))
    #print(movies_in_theater())
