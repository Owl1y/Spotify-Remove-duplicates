from spotify_client import SpotifyAPI
import json

with open("client_nums.txt", "r") as client_nums:
    lines = client_nums.readlines()
    lines = [line.rstrip() for line in lines]

# print(client_nums.readlines())

client_id = lines[0] 
client_secret = lines[1]

client = SpotifyAPI(client_id, client_secret)
client.perform_auth()
playlist_search = client.get_playlist(playlist_id='2oZKIhUbYpl5SZbUNks10k')
# print(json.dumps(playlist_search, indent=2))
print(len(playlist_search['items']))
print(playlist_search['total']) 

client_nums.close()
