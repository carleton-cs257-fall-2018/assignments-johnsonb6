#!/usr/bin/env python3
'''
    api-test.py
    Alexis Engel, Brennan Johnson, and Silas Monahan


'''

import sys
import argparse
import json
import urllib.request
import random


def get_top_movies():
	# gives you a list of top movies
	base_url = 'https://api.themoviedb.org/3/movie/popular?api_key=89036379e923b4f7b34eaa4b513982e5'
	#url = base_url.format(movies)
	movie_title_list = []

	data_from_server = urllib.request.urlopen(base_url).read()
	string_from_server = data_from_server.decode('utf-8')
	top_movies = json.loads(string_from_server)

	movie_list = top_movies["results"]
	for movie in movie_list:
		movie_title_list.append(movie["title"])

	return movie_title_list


def movies_in_theater():
	# returns a list of movies in theaters
	base_url = 'https://api.themoviedb.org/3/movie/now_playing?api_key=89036379e923b4f7b34eaa4b513982e5&language=en-US'
	#url = base_url.format(movies)
	movie_title_list = []

	data_from_server = urllib.request.urlopen(base_url).read()
	string_from_server = data_from_server.decode('utf-8')
	movies_in_theaters = json.loads(string_from_server)

	movie_list = movies_in_theaters["results"]
	for movie in movie_list:
		movie_title_list.append(movie["original_title"])

	return movie_title_list


def get_budget_for_movie(movie_id):


	base_url = 'https://api.themoviedb.org/3/movie/'+str(movie_id)+'?api_key=89036379e923b4f7b34eaa4b513982e5&language=en-US'
	#url = base_url.format()

	data_from_server = urllib.request.urlopen(base_url).read()
	string_from_server = data_from_server.decode('utf-8')
	movie_name = json.loads(string_from_server)["title"]
	movie_budget = json.loads(string_from_server)["budget"]

	return movie_name, movie_budget


def main(args):
    if args.action == 'movies_in_theater':
        print(movies_in_theater())
    elif args.action == 'get_top_movies':
        print(get_top_movies())
    elif args.action == 'get_random_movie_budget':
    	i_d = int(random.randint(1, 5000000))
    	print(get_budget_for_movie(i_d))





if __name__ == '__main__':

    api_key = '89036379e923b4f7b34eaa4b513982e5'

    parser = argparse.ArgumentParser(description='Get movie info from the IMDB API')
    parser.add_argument('action', metavar = 'action', help = "usage: 'movies_in_theater', 'get_top_movies'", choices = ["movies_in_theater", "get_top_movies", "get_random_movie_budget"])
    #if args.action == 'get budget':
    #parser.add_argument('-movie_id_number', type = int, metavar = 'movie_id_number', help = "usage: enter an integer movie id number", choices = range(1,500000000))#, choices = [None, ""])
    args = parser.parse_args()
    main(args)
    """
    i = int(sys.argv[1])
    print(i)
    movie_id = i
    print(get_budget_for_movie(movie_id))
    #print(movies_in_theater())
    print(get_top_movies())
	"""
