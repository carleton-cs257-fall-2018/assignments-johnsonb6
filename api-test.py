#!/usr/bin/env python3
'''
    api-test.py
    Alexis Engel, Brennan Johnson, and Silas Monahan


'''

import sys
import argparse
import json
import urllib.request


"""def translate_artist_id(artist_name):
	artist_id = artist_name # need to change this somehow
	'''
	user will have inputted an artist. This function will translate the name of the artist
	into the artist ID (to put into get_artist())
	'''

	return artist_id

	'''
	new_artist_ids = ""
	for i_d in artist_ids:
		new_id = translate_artist_id(i_d)
		new_artist_ids += "," + new_id
	'''
	"""

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
	# returns a list of movies in theaters

	base_url = 'https://api.themoviedb.org/3/movie/24?api_key=89036379e923b4f7b34eaa4b513982e5&language=en-US'
	#url = base_url.format()

	data_from_server = urllib.request.urlopen(base_url).read()
	string_from_server = data_from_server.decode('utf-8')
	movie_name = json.loads(string_from_server)["title"]
	movie_budget = json.loads(string_from_server)["budget"]

	return movie_name, movie_budget



if __name__ == '__main__':

	api_key = '89036379e923b4f7b34eaa4b513982e5'
	#parser = argparse.ArgumentParser(description='Get artist info from the Spotify API')
	i = int(sys.argv[1])
	print(i)
	movie_id = i
	print(get_budget_for_movie(movie_id))

	print(movies_in_theater())