# I am trying to get my code from tekore-testGH.ipynb into this one file, i pray it works
import tekore as tk
import json


with open("client_nums.txt", "r") as client_nums:
    lines = client_nums.readlines()
    lines = [line.rstrip() for line in lines]

user_id = "https://open.spotify.com/user/2153lsupa5hschcs774poensq?si=765b0985ebdc45c1"
user_id_cut = user_id[30:55]
client_id = lines[0]
client_secret = lines[1]
redirect_uri = "https://github.com/Owl1y/Spotify-Plalylist-Search"
conf = (client_id, client_secret, redirect_uri)
scoped = tk.scope.playlist_read_collaborative + tk.scope.playlist_read_private
token = tk.prompt_for_user_token(*conf, scope=scoped)
spotify = tk.Spotify(token)
playlist = spotify.playlists(user_id_cut)
client = tk.Spotify(token)


users_playlist = {}
for collections in playlist.items:
    users_playlist[collections.name] = collections.id

list_of_keys = list(users_playlist.keys())

for stuff in enumerate(list_of_keys):
    print(stuff)
    
x = [int(x) for x in input("Enter the associated number to the playlist you want analyzed(seperated by spaces): ").split()]
print("Number of list is: ", x) 

wanted_playlist = []
for playlist_titles in x:
    wanted_scan_playlist = users_playlist[list_of_keys[playlist_titles]]
    #print(users_playlist[list_of_keys[playlist_titles]])
    wanted_playlist.append(wanted_scan_playlist)
    
def get_the_playlists_info(the_playlist):
    play_offset =0
    playlist_info = {}   
    
    playlist_songs = client.playlist_items(the_playlist, as_tracks=False, offset=play_offset)
    full_list = playlist_songs.total

    while full_list != len(playlist_info):
        for songs in playlist_songs.items:
            song_name = songs.track.name
            song_artist = songs.track.artists[0].name
            playlist_info.update({song_name: song_artist})
        play_offset+=100
        playlist_songs = client.playlist_items(the_playlist, as_tracks=False, offset=play_offset)
    return playlist_info

final_play_dict = {}
for i in wanted_playlist:
    partial_play_dict = get_the_playlists_info(i)
    final_play_dict |= partial_play_dict

print(json.dumps(final_play_dict, indent=2))
