# Daily log of this project

### July 12, 2022
- I am a bit late to do a daily log of this project but I just needed something to write down my progress.
- I tried to do a simple update to the json to get the full playlist instead of just 100 songs
- lost on how to do that so next goal is to work on that
- [ ] add more than 100 songs when requestion json form spotify 

### July 14, 2022
- I think ill move to use [tekore](https://tekore.readthedocs.io/en/stable/examples/scripts/play_saved_album.html)

### July 15, 2022
- I got tekore to give me back a response of all my playlists I follow and collaborate on.
- [ ] next step is to get a playlist and all of the songs on the playlist beyond the 100 song limit

### July 16, 2022
- I got tekore to print the name of the song
- Today was very on and off, I would work for 5 leave for 50 come back for 10 and leave for 2hr
- [ ] Next step is to print the artist who made the song alongside the name of the song

### July 20, 2022
- forgot to log yesterday 
- figures out how to get the artist name from the playlist
- need to now just get all items in the playlist, not just the 100 limit
  - I tried to do a for loop but it is not working, I will figure this out though

### July 21, 2022
- I unironically have no idea what I am doing wrong. 
- I have a for loop running and getting each of the songs and artist
  - the dict I put it into gets all the data
  - I think the problem is that the while loop is not broken
    - I tested the while loop with a print statement and I think the while loop is infinite

### July 22, 2022
- I finally got it to get the entire playlist
  - Both the song name and the songs artist


### July 24, 2022
- I finally got it to print out each of the playlist from a list
- Later on I also got the data into one dict instead of multiple dict responses
  - shout out to [this](https://towardsdatascience.com/merge-dictionaries-in-python-d4e9ce137374) for telling me how to combine dicts
- tomorrow I will try to get input from a user instead of just having hardcoded links

### July 25, 2022
- Did today
  - I was able to get a users id and scan the playlist they made and follow
- todo
  - need to have the ability to choose which playlist you want scanned 


### July 31, 2022
- Did today
  - Got users playlist and put them in a dictonary
  - was able to make the key value the playlist id
- todo
  - pick what playlist you want in the dictonary and it takes the playlist id

### October 5, 2022
- I really added nothing. I am just trying to get the users playlist and then have them answer which ones they want scanned


### October 21, 2022
- I got the program to do the biggest thing
  1. ask user for their id
  2. scan the playlist the owner owns
  3. show the user the playlist they own
  4. ask them which playlist they want to be scanned
  5. gets that input and scans the playlist they selected

### December 18, 2022
- The program is now conected
  - this means it can get a user
  - read their playlist
  - ask the person running the program what playlist they want scanned
  - it scans the playlist and returns the items in the playlist


### December 21, 2022
- Program now gets back the song id


### December 22, 2022
- it now can read the playlist(s), get their song id's, and inputs it into one playlist
- with help to this code 
```python
for i in range(0, len(final_ids), 100):
    start = i
    fin = 100 + i
    client.playlist_add(theee_playlist, final_ids[start:fin], position=0)

```
