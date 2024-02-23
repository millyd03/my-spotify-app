from library.artists import Artists
from library.auth import Auth
from library.songs import Songs
from library.podcasts import Podcasts
from library.playlists import Playlists
from datetime import datetime
import yaml

config_file = "../config/config.yml"

with open(config_file, "r") as file:
    config_data = yaml.safe_load(file)

manual = False
playlist_id = None
today = datetime.today()
weekday_name = today.strftime("%A")
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
        tracks.append(f"spotify:track:{song["id"]}")
        print(idx, song["artists"][0]["name"], song["name"])

    playlists.add_to_playlist(playlist_id, tracks)

    for idx, podcast in enumerate(followed_podcasts):
        if podcast["show"]["name"] == "Up First":
            todays_shows = podcasts.get_podcast_recent_episodes(podcast["show"]["id"], 1)
            playlists.add_to_playlist(playlist_id, [f"spotify:episode:{todays_shows["items"][0]["id"]}"], 0)
            print(0, podcast["show"]["name"], todays_shows["items"][0]["name"])
        if podcast["show"]["name"] == "The Journal.":
            todays_shows = podcasts.get_podcast_recent_episodes(podcast["show"]["id"], 1)
            playlists.add_to_playlist(playlist_id, [f"spotify:episode:{todays_shows["items"][0]["id"]}"], 6)
            print(6, podcast["show"]["name"], todays_shows["items"][0]["name"])

if 10 < current_hour or manual:
    if playlist_id is None:
        for idx, playlist in enumerate(my_playlists):
            if "name" in playlist and playlist["name"] == f"My {weekday_name} Drive":
                playlist_id = playlist["id"]
                break

    for idx, podcast in enumerate(followed_podcasts):
        if podcast["show"]["name"] == "Klein/Ally Show: The Podcast":
            if weekday_name == "Wednesday":
                todays_shows = podcasts.get_podcast_recent_episodes(podcast["show"]["id"], 4)
                playlists.add_to_playlist(playlist_id, [f"spotify:episode:{todays_shows["items"][3]["id"]}"], 17)
                print(17, podcast["show"]["name"], todays_shows["items"][3]["name"])
                playlists.add_to_playlist(playlist_id, [f"spotify:episode:{todays_shows["items"][2]["id"]}"], 27)
                print(27, podcast["show"]["name"], todays_shows["items"][2]["name"])
                playlists.add_to_playlist(playlist_id, [f"spotify:episode:{todays_shows["items"][0]["id"]}"], 37)
                print(37, podcast["show"]["name"], todays_shows["items"][0]["name"])
            else:
                todays_shows = podcasts.get_podcast_recent_episodes(podcast["show"]["id"], 3)
                playlists.add_to_playlist(playlist_id, [f"spotify:episode:{todays_shows["items"][2]["id"]}"], 17)
                print(17, podcast["show"]["name"], todays_shows["items"][2]["name"])
                playlists.add_to_playlist(playlist_id, [f"spotify:episode:{todays_shows["items"][1]["id"]}"], 27)
                print(27, podcast["show"]["name"], todays_shows["items"][1]["name"])
