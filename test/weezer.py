from utility.auth import Auth
import yaml

from utility.songs import Songs

config_file = "../config/config.yml"

with open(config_file, "r") as file:
    config_data = yaml.safe_load(file)

auth = Auth(config_data["client_id"], config_data["client_secret"], config_data["redirect_uri"])
sp = auth.get_spotify_connection_with_authorization_code()

user_info = sp.current_user()
print(user_info["id"], user_info["display_name"])

cache_file = "../cache/artist_tracks_cache"

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])

songs = Songs(sp)

print("\nTop Songs:")
top_tracks = songs.get_artists_top_songs('3jOstUTkEu2JkjvRdBA5Gu')
for idx, top_track in enumerate(top_tracks['tracks']):
    print(idx, top_track)

print("\nAll Songs:")
all_tracks = songs.get_all_artists_songs('Weezer', cache_file)
for idx, track in enumerate(all_tracks):
    print(idx, track)

print("\nFresh Songs:")
freshest_tracks = songs.get_top_new_songs('Weezer', cache_file)
for idx, fresh_track in enumerate(freshest_tracks):
    print(idx, fresh_track['name'])

print("\nOld Songs:")
oldest_tracks = songs.get_top_old_songs('Weezer', cache_file)
for idx, old_track in enumerate(oldest_tracks):
    print(idx, old_track['name'])
