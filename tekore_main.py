import tekore as tk
import base64
import requests
import datetime
from urllib.parse import urlencode
from inspect import signature
import json
import time

with open("client_nums.txt", "r") as client_nums:
    lines = client_nums.readlines()
    lines = [line.rstrip() for line in lines]

client_id = lines[0]
client_secret = lines[1]
redirect_uri = "https://github.com/Owl1y/Spotify-Plalylist-Search"

conf = (client_id, client_secret, redirect_uri)
scoped = tk.scope.playlist_read_collaborative + tk.scope.playlist_read_private
token = tk.prompt_for_user_token(*conf)
client = tk.Spotify(token)

id_of_playlists = [
    "https://open.spotify.com/playlist/7IHZvZIusTuJNMcKleSWwd?si=e04af12a619844fd",
    "https://open.spotify.com/playlist/6fYjLM7ESHGrh5N9SvzVGB?si=0449e736c1fc407c",
    "https://open.spotify.com/playlist/77sj0Sh0vzMlWnV7SlqkLu?si=421859b79e3849dc",
    "https://open.spotify.com/playlist/40daaNzvSSvYGIZhqX7HsR?si=b82d43ddedbd452c",
    "https://open.spotify.com/playlist/26ZzwXAOlKTvsVjQcQd4gm?si=6a7f4b03aaeb4473",
    "https://open.spotify.com/playlist/7jXzoKibDwt7yYaoU3uPdF?si=bf78d39da0a2482a",
]
playlist_cut = [cuts[34:56] for cuts in id_of_playlists]


def get_the_playlists_info(the_playlist):
    play_offset = 0
    playlist_info = {}

    playlist_songs = client.playlist_items(
        the_playlist, as_tracks=False, offset=play_offset
    )
    full_list = playlist_songs.total

    while full_list != len(playlist_info):
        for songs in playlist_songs.items:
            song_name = songs.track.name
            song_artist = songs.track.artists[0].name
            playlist_info.update({song_name: song_artist})
        play_offset += 100
        playlist_songs = client.playlist_items(
            the_playlist, as_tracks=False, offset=play_offset
        )
    return playlist_info


final_play_dict = {}
for i in playlist_cut:
    partial_play_dict = get_the_playlists_info(i)
    final_play_dict |= partial_play_dict

print(final_play_dict)


client_nums.close()
