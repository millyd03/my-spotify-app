import yaml

from utility.artists import Artists
from utility.auth import Auth
from utility.playlists import Playlists

config_file = "../config/config.yml"

with open(config_file, "r") as file:
    config_data = yaml.safe_load(file)

auth = Auth(config_data["client_id"], config_data["client_secret"], config_data["redirect_uri"])
sp = auth.get_spotify_connection_with_authorization_code()

artists = Artists(sp)
followed_artists = artists.get_my_followed_artists()
selected_artists = []
for idx, artist in enumerate(followed_artists):
    selected_artists.append(followed_artists["id"])
    print("\"" + artist["id"] + "\"")

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

playlists = Playlists(sp)
playlists.create_daily_drive_playlist(50, 5, selected_artists, included_podcasts, False)
