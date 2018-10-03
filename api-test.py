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
    	i_d = int(random.randint(1, 250))
    	print(i_d)
    	
    	works = False
    	while not works:
    		try:
    			print(get_budget_for_movie(i_d))
    			works = True
    		except:
    			i_d = int(random.randint(1, 250))


if __name__ == '__main__':

    api_key = '89036379e923b4f7b34eaa4b513982e5'

    parser = argparse.ArgumentParser(description='Get movie info from the IMDB API')
    parser.add_argument('action', metavar = 'action', help = "usage: 'movies_in_theater', 'get_top_movies'", choices = ["movies_in_theater", "get_top_movies", "get_random_movie_budget"])
    args = parser.parse_args()
    main(args)
