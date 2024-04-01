from utility.auth import Auth
import yaml

config_file = "../config/config.yml"

with open(config_file, "r") as file:
    config_data = yaml.safe_load(file)

auth = Auth(config_data["client_id"], config_data["client_secret"])
sp = auth.get_spotify_connection_with_credentials()

user_info = sp.current_user()
print(user_info["id"], user_info["display_name"])

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])
