from library.artists import Artists
from library.auth import Auth
from library.songs import Songs
from library.podcasts import Podcasts
from library.playlists import Playlists
from definition.day_intros import DayIntros
from datetime import datetime
import yaml
import sys

config_file = "../config/config.yml"

with open(config_file, "r") as file:
    config_data = yaml.safe_load(file)

manual = False

if len(sys.argv) > 1:
    manual = True
    weekday_name = sys.argv[1]

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
followed_podcasts = podcasts.get_my_followed_podcasts("US")

playlists = Playlists(sp)
my_playlists = playlists.get_my_playlists()

# Start with 50 songs
if current_hour < 10 or manual:
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

    playlists.add_to_playlist(playlist_id, tracks)
    day_intro_enum = getattr(DayIntros, weekday_name.upper(), None)
    if day_intro_enum is not None and len(day_intro_enum.value) > 0:
        playlists.add_to_playlist(playlist_id, ["spotify:track:" + day_intro_enum.value], 0)

    for idx, podcast in enumerate(followed_podcasts):
        if podcast["show"]["name"] == "Up First":
            if manual:
                todays_show = podcasts.get_podcast_from_past_weeks_day(podcast["show"]["id"], weekday_name)
            else:
                todays_show = podcasts.get_podcast_recent_episodes(podcast["show"]["id"], 1)
            playlists.add_to_playlist(playlist_id, ["spotify:episode:" + todays_show[0]["id"]], 1)
            print(podcast["show"]["name"], todays_show[0]["name"])
        if podcast["show"]["name"] == "The Journal.":
            if manual:
                todays_show = podcasts.get_podcast_from_past_weeks_day(podcast["show"]["id"], weekday_name)
            else:
                todays_show = podcasts.get_podcast_recent_episodes(podcast["show"]["id"], 1)
            playlists.add_to_playlist(playlist_id, ["spotify:episode:" + todays_show[0]["id"]], 7)
            print(podcast["show"]["name"], todays_show[0]["name"])

if 10 <= current_hour or manual:
    if playlist_id is None:
        for idx, playlist in enumerate(my_playlists):
            if "name" in playlist and playlist["name"] == f"My {weekday_name} Drive":
                playlist_id = playlist["id"]
                break

    for idx, podcast in enumerate(followed_podcasts):
        if podcast["show"]["id"] == "1qf16YCjKMzkjuxsThySIC":
            if weekday_name == "Wednesday":
                todays_shows = podcasts.get_podcast_recent_episodes(podcast["show"]["id"], 4)
                playlists.add_to_playlist(playlist_id, ["spotify:episode:" + todays_shows[3]["id"]], 18)
                print(podcast["show"]["name"], todays_shows[3]["name"])
                playlists.add_to_playlist(playlist_id, ["spotify:episode:" + todays_shows[2]["id"]], 28)
                print(podcast["show"]["name"], todays_shows[2]["name"])
                playlists.add_to_playlist(playlist_id, ["spotify:episode:" + todays_shows[0]["id"]], 38)
                print(podcast["show"]["name"], todays_shows[0]["name"])
            else:
                todays_shows = podcasts.get_podcast_recent_episodes(podcast["show"]["id"], 3)
                playlists.add_to_playlist(playlist_id, ["spotify:episode:" + todays_shows[2]["id"]], 18)
                print(podcast["show"]["name"], todays_shows[2]["name"])
                playlists.add_to_playlist(playlist_id, ["spotify:episode:" + todays_shows[1]["id"]], 28)
                print(podcast["show"]["name"], todays_shows[1]["name"])
