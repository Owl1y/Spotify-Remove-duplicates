import tekore as tk

with open("client_nums.txt", "r") as client_nums:
    lines = client_nums.readlines()
    lines = [line.rstrip() for line in lines]

client_id = lines[0]
client_secret = lines[1]
redirect_uri = "https://github.com/Owl1y/Spotify-Plalylist-Search"


conf = (client_id, client_secret, redirect_uri)
scoped = tk.scope.playlist_read_collaborative + tk.scope.playlist_read_private
token = tk.prompt_for_user_token(*conf, scope=scoped)


spotify = tk.Spotify(token)
playlist = spotify.playlists("2153lsupa5hschcs774poensq")
for collections in playlist.items:
    print(f"{collections.name}- {collections.description}")
