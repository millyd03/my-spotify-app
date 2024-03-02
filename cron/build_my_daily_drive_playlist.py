from utility.artists import Artists
from utility.auth import Auth
from utility.songs import Songs
from utility.podcasts import Podcasts
from utility.playlists import Playlists
from definition.day_intros import DayIntros
from datetime import datetime
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

playlist_id = None
current_time = datetime.now()
current_hour = current_time.hour

auth = Auth(config_data["client_id"], config_data["client_secret"], config_data["redirect_uri"])
sp = auth.get_spotify_connection_with_authorization_code()

user_info = sp.current_user()
print(f"Hello, {user_info['display_name']}!")
print(f"Here's your updated playlist for {weekday_name}:")

artists = Artists(sp)
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
included_podcasts = [podcast_1, podcast_2, podcast_3, podcast_4, podcast_5, podcast_6]
songs_between = 5

playlists = Playlists(sp)
my_playlists = playlists.get_my_playlists()

# Start with 50 songs
for idx, playlist in enumerate(my_playlists):
    if "name" in playlist and playlist["name"] == f"My {weekday_name} Drive":
        playlists.delete_playlist(playlist["id"])
        break

playlist_id = playlists.create_playlist(f"My {weekday_name} Drive")

songs = Songs(sp)
playlist_songs = songs.get_random_songs(followed_artists, 50)

tracks = []
for idx, song in enumerate(playlist_songs):
    tracks.append("spotify:track:" + song["id"])
    print(idx, song["artists"][0]["name"], song["name"])

if not debug:
    playlists.add_to_playlist(playlist_id, tracks)
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
        if todays_show[0]["duration_ms"] > 1800000:
            chunks = int(todays_show[0]["duration_ms"] / 1800000)
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
