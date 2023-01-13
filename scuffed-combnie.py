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

scoped = tk.scope.playlist_read_collaborative + tk.scope.playlist_read_private + tk.scope.playlist_modify_public
token = tk.prompt_for_user_token(*conf, scope=scoped)

#spotify = tk.Spotify(token)
client = tk.Spotify(token)
playlist = client.playlists(user_id_cut)


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

theee_playlist = "https://open.spotify.com/playlist/78KodfOBZ4qd8qLLiuFjcD?si=8113f0bb8c67496e"[34:56]
the_pl_array = [theee_playlist]
thee_pl_list = []
for index in the_pl_array:
    swag4 = get_song_ids(index)
    thee_pl_list.extend(swag4)
    
    
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
    #print(wanted_scan_playlist)
    wanted_playlist.append(wanted_scan_playlist) 
    

final_ids = []
final_play_dict = {}
for i in wanted_playlist:
    partial_play_dict, partial_song_id = get_playlist_info(i)
    final_ids.extend(partial_song_id)
    final_play_dict |= partial_play_dict

print(len(final_ids))

resulting_pl = [z for z in final_ids if z not in thee_pl_list]

print(len(resulting_pl))

for i in range(0, len(resulting_pl), 100):
    start = i
    fin = 100 + i
    client.playlist_add(theee_playlist, resulting_pl[start:fin], position=0)
    #print(final_ids[start:fin])




