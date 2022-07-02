from spotify_client import SpotifyAPI
import json
# import pandas as pd

with open("client_nums.txt", "r") as client_nums:
    lines = client_nums.readlines()
    lines = [line.rstrip() for line in lines]

# print(client_nums.readlines())

client_id = lines[0] 
client_secret = lines[1]

client = SpotifyAPI(client_id, client_secret)
client.perform_auth()
track_search = client.search({"album":"my beautiful dark", "artist":"kanye"}, search_type="album")
track_in_json = json.dumps(track_search, indent=2)
print(track_in_json)

# for song in track_in_json:
#     print(song[''])
#print(type(track_search))
# df = pd.read_json(track_in_json, orient='columns')
# print(df)
client_nums.close()
