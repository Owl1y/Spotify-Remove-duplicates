#!/usr/bin/env python
# coding: utf-8
# In[1]:
import tekore as tk
import json
import random
# In[2]:
with open("client_nums.txt", "r") as client_nums:
    lines = client_nums.readlines()
    lines = [line.rstrip() for line in lines]

user_id = "https://open.spotify.com/user/2153lsupa5hschcs774poensq?si=765b0985ebdc45c1"
user_id_cut = user_id[30:55]

client_id = lines[0]
client_secret = lines[1]
redirect_uri = "https://github.com/Owl1y/Spotify-Plalylist-Search"
conf = (client_id, client_secret, redirect_uri)

scoped = tk.scope.playlist_read_collaborative + tk.scope.playlist_read_private + tk.scope.playlist_modify_public
token = tk.prompt_for_user_token(*conf, scope=scoped)

#spotify = tk.Spotify(token)
client = tk.Spotify(token)
playlist = client.playlists(user_id_cut)
# In[3]:

# function cells
def get_playlist_info(the_playlist):
    song_ids = []
    play_offset =0
    playlist_info = {}   
    
    playlist_songs = client.playlist_items(the_playlist, as_tracks=False, offset=play_offset)
    full_list = playlist_songs.total

    while full_list != len(playlist_info):
        for songs in playlist_songs.items:
            song_name = songs.track.name
            song_artist = songs.track.artists[0].name
            song_id = songs.track.uri
            song_ids.append(song_id)
            playlist_info.update({song_name: song_artist})
        play_offset+=100
        playlist_songs = client.playlist_items(the_playlist, as_tracks=False, offset=play_offset)
    return playlist_info, song_ids

def get_song_ids(the_playlist):
    song_ids = []
    play_offset =0 
    
    playlist_songs = client.playlist_items(the_playlist, as_tracks=False, offset=play_offset)
    full_list = playlist_songs.total

    while full_list != len(song_ids):
        for songs in playlist_songs.items:
            song_id = songs.track.uri
            song_ids.append(song_id)
            #print(song_id)
        play_offset+=100
        playlist_songs = client.playlist_items(the_playlist, as_tracks=False, offset=play_offset)
    return song_ids
# In[4]:
former_playlist = ['7IHZvZIusTuJNMcKleSWwd', 
                   '6fYjLM7ESHGrh5N9SvzVGB', 
                   '77sj0Sh0vzMlWnV7SlqkLu', 
                   '40daaNzvSSvYGIZhqX7HsR', 
                   '26ZzwXAOlKTvsVjQcQd4gm', 
                   '7jXzoKibDwt7yYaoU3uPdF', 
                   '0AFQ3bdD6zCyXda4FOwp39']

current_playlist = ['5TMatpArr9xKImvUHGydS8']

# godder than a mug--> 5TMatpArr9xKImvUHGydS8
# In[5]:
current_pl_uris = get_song_ids(current_playlist[0])

for nums in former_playlist:
    former_pl_uris = get_song_ids(nums)
    duplicate_uris = [songs for songs in former_pl_uris if songs in current_pl_uris]
    client.playlist_remove(current_playlist[0], duplicate_uris)
    
    print(duplicate_uris)

