#!/usr/bin/env python3
'''
    api-test.py
    Alexis Engel, Brennan Johnson, and Silas Monahan


'''

import sys
import argparse
import json
import urllib.request


def translate_artist_id(artist_name):
	artist_id = artist_name # need to change this somehow
	'''
	user will have inputted an artist. This function will translate the name of the artist
	into the artist ID (to put into get_artist())
	'''

	return artist_id


def get_artists(artist_ids):
	# gives you a list of artists
	new_artist_ids = ""
	for i_d in artist_ids:
		new_id = translate_artist_id(i_d)
		new_artist_ids += "," + new_id


	base_url = https://api.spotify.com/v1/artists/{new_artist_ids}
	url = base_url.format(artists)

	data_from_server = urllib.request.urlopen(url).read()
    string_from_server = data_from_server.decode('utf-8')
    artists = json.loads(string_from_server)

    # returns an array of artist objects
    return artists


def get_artist_top_tracks(artist_name):
	# returns a list of a specific atrist's top tracks
	artist_id = translate_artist_id(artist_name)
	base_url = https://api.spotify.com/v1/artists/{artist_id}/top-tracks
	url = base_url.format(tracks)

	data_from_server = urllib.request.urlopen(url).read()
    string_from_server = data_from_server.decode('utf-8')
    top_tracks = json.loads(string_from_server)


    # returns a list of up to 10 track objects
    return top_tracks



def get_artist(artist_id):
	base_url = https://api.spotify.com/v1/artists/{artist_id}
	url = base_url.format(artist)

	data_from_server = urllib.request.urlopen(url).read()
    string_from_server = data_from_server.decode('utf-8')
    artist = json.loads(string_from_server)

    # returns an artist object
    return artist


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Get artist info from the Spotify API')

	parser.add_argument('artist name',
                        metavar='artist name',
                        help='the artists name that you want to get information on',
                        #choices=['root', 'conjugate']
                        )

	parser.add_argument('top tracks',
                        metavar='top tracks',
                        help='if you want to find the atrists top tracks',
                        choices=['top tracks'])
	
	'''
	artist_name = args[0]
	if args[1] != None:
		get_artist_top_tracks(args[0])
	'''