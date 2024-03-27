from utility.auth import Auth
from utility.podcasts import Podcasts
import yaml

config_file = "../config/config.yml"

with open(config_file, "r") as file:
    config_data = yaml.safe_load(file)

auth = Auth(config_data["client_id"], config_data["client_secret"], config_data["redirect_uri"])
sp = auth.get_spotify_connection_with_authorization_code()

podcasts = Podcasts(sp)
followed_podcasts = podcasts.get_my_followed_podcasts()

for idx, podcast in enumerate(followed_podcasts):
    print(podcast["show"]["id"], podcast["show"]["name"])

episode = podcasts.get_podcast_oldest_unplayed_episode("5PGmCKE1KzIHMN9kvKOpC8")
