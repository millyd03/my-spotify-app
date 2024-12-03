from utility.auth import Auth
from utility.playlists import Playlists
from utility.songs import Songs
import yaml

config_file = "../config/config.yml"

with open(config_file, "r") as file:
    config_data = yaml.safe_load(file)

auth = Auth(config_data["client_id"], config_data["client_secret"], config_data["redirect_uri"])
sp = auth.get_spotify_connection_with_authorization_code()

playlists = Playlists(sp)

my_playlists = playlists.get_my_playlists()

for idx, playlist in enumerate(my_playlists):
    if playlist is not None:
        print(playlist['name'], playlist['id'])

#songs = Songs(sp)
#playlist_songs = songs.get_playlist_songs('1iOmFONzHZlqggYum8UHKH')

#for idx, song in enumerate(playlist_songs):
#    if song is not None:
#        print(song)