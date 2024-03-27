from utility.artists import Artists
from utility.auth import Auth
import yaml

config_file = "../config/config.yml"

with open(config_file, "r") as file:
    config_data = yaml.safe_load(file)

auth = Auth(config_data["client_id"], config_data["client_secret"], config_data["redirect_uri"])
sp = auth.get_spotify_connection_with_authorization_code()
user = sp.current_user()
artists = Artists(sp)
followed_artists = artists.get_my_followed_artists()

for idx, artist in enumerate(followed_artists):
    print(artist["id"], artist["name"])
