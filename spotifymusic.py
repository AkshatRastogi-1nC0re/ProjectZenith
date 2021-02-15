# Import libraries
import os
import json
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError
import time
import random


username = "s3065non0v0aqxfotu7mb8hh0"
SPOTIPY_CLIENT_ID = "d489f373053c426eb8f8db9ed4ca4d60"
SPOTIPY_CLIENT_SECRET = "86da1cbc169140fc8232a614522052b8"
SPOTIPY_REDIRECT_URI = "https://www.google.co.in/"
scope = 'user-read-private user-read-playback-state user-modify-playback-state'




def spotipy_lol(artist_name):
    try:
        token = util.prompt_for_user_token(username, scope)
    except (AttributeError, JSONDecodeError):
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, scope)

    spotifyObject = spotipy.Spotify(auth=token)

    devices = spotifyObject.devices()
    print(json.dumps(devices, sort_keys=True, indent=4))
    deviceID = devices['devices'][0]['id']

    # Get track information
    track = spotifyObject.current_user_playing_track()
    print(json.dumps(track, sort_keys=True, indent=4))
    print()
    artist = track['item']['artists'][0]['name']
    track = track['item']['name']

    if artist !="":
        f = open('text_to_print.txt', 'w')
        f.write(str("Currently playing " + artist + " - " + track))
        f.close()

    # User information
    user = spotifyObject.current_user()
    displayName = user['display_name']
    follower = user['followers']['total']

    while True:
        searchQuery = artist_name ## def
        searchResults = spotifyObject.search(searchQuery, 1, 0, "artist")
        # Print artist details
        artist = searchResults['artists']['items'][0]
        artistID = artist['id']
        # Album details
        trackURIs = []
        trackArt = []
        z = 0
        # Extract data from album
        albumResults = spotifyObject.artist_albums(artistID)
        albumResults = albumResults['items']

        for item in albumResults:
            f = open('text_to_print.txt', 'w')
            f.write("ALBUM: " + item['name'])
            f.close()
            albumID = item['id']
            albumArt = item['images'][0]['url']

            # Extract track data
            trackResults = spotifyObject.album_tracks(albumID)
            trackResults = trackResults['items']

            for item in trackResults:
                f = open('text_to_print.txt', 'w')
                f.write(str(str(z) + ": " + item['name']))
                f.close()
                trackURIs.append(item['uri'])
                trackArt.append(albumArt)
                z += 1
        for n in range(1,20):
            songSelection = n
            trackSelectionList = []
            trackSelectionList.append(trackURIs[int(songSelection)])
            spotifyObject.start_playback(deviceID, None, trackSelectionList)
            time.sleep(200)
