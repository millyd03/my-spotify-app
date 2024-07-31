from definition.song_filters import SongFilters
from utility.artists import Artists
from utility.auth import Auth
from utility.songs import Songs
from utility.podcasts import Podcasts
from utility.playlists import Playlists
from definition.day_intros import DayIntros
from datetime import datetime
from utility.spotipy_facade import current_user
import yaml
import sys

config_file = "../config/config.yml"

with open(config_file, "r") as file:
    config_data = yaml.safe_load(file)

manual = False
debug = False

if len(sys.argv) > 1:
    debug = bool(sys.argv[1])

if len(sys.argv) > 2:
    manual = True
    weekday_name = sys.argv[2]
else:
    today = datetime.today()
    weekday_name = today.strftime("%A")

auth = Auth(config_data["client_id"], config_data["client_secret"], config_data["redirect_uri"])
sp = auth.get_spotify_connection_with_authorization_code()

user_info = current_user(sp)
print(f"Hello, {user_info['display_name']}!")

artists = Artists(sp)
favorite_artists = ['3jOstUTkEu2JkjvRdBA5Gu',  #Weezer
                    '7oPftvlwr6VrsViSDV7fJY',  #Green Day
                    '4ghjRm4M2vChDfTUycx0Ce',  #New Found Glory
                    '6FBDaR13swtiWwGhX1WQsP',  #blink-182
                    '3Ayl7mCk0nScecqOzvNp6s',  #Jimmy Eat World
                    '54Bjxn26WsjfslQbNVtSCm',  #The Get Up Kids
                    '0eW6yRE8ePadhUe1Numam9',  #Sherwood
                    '6VLj1qK2dmR3P2yMNTSn2Y',  #Bleach
                    '1sxRcl7G7tpQvuQkMyAWau',  #Slick Shoes
                    '1Enp9WKfk0aI9CFi2YGBq7',  #Further Seems Forever
                    '3nJWBJvK7uGvfp4iZh9CkN',  #Relient K
                    '0qT79UgT5tY4yudH9VfsdT',  #Sum 41
                    '3lqHnJKd9fNQEV7Ewcd0Ge',  #Dogwood
                    '0FguhfqSypXh6FuYJHkI6w',  #Children 18:3
                    '7zn1qF9KcBCxwj2Rpn4fAp',  #Over It
                    '1aEYCT7t18aM3VvM6y8oVR',  #Alkaline Trio
                    '3zxKH0qp3nBCuPZCZT5Vaf'   #Yellowcard
                    ]
followed_artists = artists.get_my_followed_artists()

podcasts = Podcasts(sp)
podcast_1 = {
    "id": "2mTUnDkuKUkhiueKcVWoP0",
    "backup": None,
    "name": "Up First",
    "most_recent": True
}
podcast_2 = {
    "id": "2oQATctoAaFiS8bT596v9G",
    "backup": None,
    "name": "The Fr. Mike Schmitz Catholic Podcast",
    "most_recent": False
}
podcast_3 = {
    "id": "1qf16YCjKMzkjuxsThySIC",
    "backup": None,
    "name": "Klein. Alley. Show.",
    "most_recent": True
}
podcast_4 = {
    "id": "0KxdEdeY2Wb3zr28dMlQva",
    "backup": None,
    "name": "The Journal",
    "most_recent": True
}
podcast_5 = {
    "id": "5PGmCKE1KzIHMN9kvKOpC8",
    "backup": None,
    "name": "The Council of Trent Podcast",
    "most_recent": False
}
podcast_6 = {
    "id": "0FGOz929il130iXEwkInBa",
    "backup": None,
    "name": "Hello From the Magic Tavern",
    "most_recent": False
}
podcast_7 = {
    "id": "7nqJajzyZo3gdisGk7XhQx",
    "backup": {
        "id": "53dHyhzazFrmPhwuambyuM",
        "backup": {
            "id": "0sxpFsg449GC8TPtrRVCUW",
            "backup": None,
            "name": "The Weekly Show with Jon Stewart",
            "most_recent": False
        },
        "name": "The Daily Show: Ears Edition",
        "most_recent": False
    },
    "name": "Real Time with Bill Maher",
    "most_recent": True
}
included_podcasts = [podcast_1, podcast_2, podcast_3, podcast_4, podcast_5, podcast_6, podcast_7]
songs_between = 3
cache_file = "../cache/artist_tracks_cache"

playlists = Playlists(sp)
my_playlists = playlists.get_my_playlists()

# Start with 50 songs
for idx, playlist in enumerate(my_playlists):
    if "name" in playlist and playlist["name"] == f"My {weekday_name} Drive":
        playlists.delete_playlist(playlist["id"])
        break

playlist_id = playlists.create_playlist(f"My {weekday_name} Drive")

song_filter = None
if weekday_name.upper() == "WEDNESDAY":
    song_filter = SongFilters.WILDCARD
elif weekday_name.upper() == "THURSDAY":
    song_filter = SongFilters.THROWBACK
elif weekday_name.upper() == "FRIDAY":
    song_filter = SongFilters.FRESH

print(f"Here's your playlist for {song_filter.value} {weekday_name}:")

songs = Songs(sp)
playlist_songs = songs.get_random_songs(followed_artists, 50, cache_file, True, {}, favorite_artists, song_filter)

tracks = []
idx = 0
for song in playlist_songs:
    if song is not None:
        tracks.append("spotify:track:" + song["id"])
        print(idx, song["artists"][0]["name"], song["name"])
        idx += 1

if not debug:
    for track in tracks:
        playlists.add_to_playlist(playlist_id, [track])
day_intro_enum = getattr(DayIntros, weekday_name.upper(), None)
if day_intro_enum is None:
    day_intro_track = "6S1kSZwTOv93ZmClI5tekm"
else:
    day_intro_track = day_intro_enum.value
if day_intro_track is not None and len(day_intro_track) > 0:
    if not debug:
        playlists.add_to_playlist(playlist_id, ["spotify:track:" + day_intro_track], 0)

location = 1
for idx, podcast in enumerate(included_podcasts):
    if podcast["most_recent"]:
        if manual:
            todays_show = podcasts.get_podcast_from_past_weeks_day(podcast["id"], weekday_name)
        else:
            todays_show = podcasts.get_podcast_recent_episodes(podcast["id"], 1)
        if todays_show[0]["duration_ms"] > 5000000:
            chunks = int(todays_show[0]["duration_ms"] / 1800000) + 1
            for n in range(chunks):
                if not debug:
                    playlists.add_to_playlist(playlist_id, ["spotify:episode:" + todays_show[0]["id"]], location)
                print(location, podcast["name"], todays_show[0]["name"])
                location += songs_between + 1
        else:
            if not debug:
                playlists.add_to_playlist(playlist_id, ["spotify:episode:" + todays_show[0]["id"]], location)
            print(location, podcast["name"], todays_show[0]["name"])
            location += songs_between + 1
    else:
        todays_show = podcasts.get_podcast_oldest_unplayed_episode(podcast["id"])
        if todays_show is not None:
            if not debug:
                playlists.add_to_playlist(playlist_id, ["spotify:episode:" + todays_show["id"]], location)
            print(location, podcast["name"], todays_show["name"])
            location += songs_between + 1
