import requests
import spotipy
import os
import dotenv
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

dotenv.load_dotenv(".env")
SPOTIPY_CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
SPOTIPY_CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
SPOTIPY_REDIRECT_URI = os.environ["SPOTIPY_REDIRECT_URI"]

# scope = "playlist-modify-private"
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " - ", track['name'])


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="playlist-read-private"))


# urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
# artist = sp.artist(urn)
# print(artist)
#
# user = sp.user('plamere')
# print(user)

def list_playlists():
    playlists = sp.current_user_playlists(limit=1)
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'], playlist['name']))
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None
    return playlists


# list_playlists()

def list_tracks_in_playlist(playlist_id):
    target_playlist = sp.playlist_items(playlist_id=playlist_id)
    for i, track in enumerate(target_playlist['items']):
        print(target_playlist.keys())
    return target_playlist


playlists = list_playlists()
# tracks = list_tracks_in_playlist("2aFkvVQiTGIDYqwbGK5rNE")

# print(target_playlist.keys())
# playlist_items = target_playlist['items']
# tracks = playlist_items.items()
# print(tracks)


# print([track for track in tracks])
#
# import json
# playlist_json = json.loads(target_playlist)
# print(playlist_json)

""""
            TO USE
===============================
playlist_add_items(playlist_id, items, position=None)
playlist_change_details(playlist_id, name=None, public=None, collaborative=None, description=None)
playlist_items(playlist_id, fields=None, limit=100, offset=0, market=None, additional_types=('track', 'episode'))

user_playlist_create(user, name, public=True, collaborative=False, description='')
user_playlist_change_details(user, playlist_id, name=None, public=None, collaborative=None, description=None)
user_playlist_add_tracks(user, playlist_id, tracks, position=None)
"""

"""
            NOT WORKING
==================================
current_track = sp.current_user_playing_track()
print(current_track)
"""
