import yaml

from utility.auth import Auth
from utility.songs import Songs

config_file = "../config/config.yml"

with open(config_file, "r") as file:
    config_data = yaml.safe_load(file)

auth = Auth(config_data["client_id"], config_data["client_secret"], config_data["redirect_uri"])
sp = auth.get_spotify_connection_with_authorization_code()

pax_217 = {'external_urls': {'spotify': 'https://open.spotify.com/artist/52BrJWa29mZPy5hgDIs6d0'}, 'followers': {'href': None, 'total': 5311}, 'genres': ['christian punk'], 'href': 'https://api.spotify.com/v1/artists/52BrJWa29mZPy5hgDIs6d0', 'id': '52BrJWa29mZPy5hgDIs6d0', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b27387dc08052e2e7ec0d5200249', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e0287dc08052e2e7ec0d5200249', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d0000485187dc08052e2e7ec0d5200249', 'width': 64}], 'name': 'Pax217', 'popularity': 18, 'type': 'artist', 'uri': 'spotify:artist:52BrJWa29mZPy5hgDIs6d0'}
songs = Songs(sp);
selected_songs = songs.get_random_songs([pax_217], 5, True, {})

idx = 0
for song in selected_songs:
    if song is not None:
        print(idx, song["artists"][0]["name"], song["name"])
        idx += 1

blink_182 = {'external_urls': {'spotify': 'https://open.spotify.com/artist/6FBDaR13swtiWwGhX1WQsP'}, 'followers': {'href': None, 'total': 8104564}, 'genres': ['alternative metal', 'modern rock', 'pop punk', 'punk', 'rock', 'socal pop punk'], 'href': 'https://api.spotify.com/v1/artists/6FBDaR13swtiWwGhX1WQsP', 'id': '6FBDaR13swtiWwGhX1WQsP', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab6761610000e5eb5da36f8b98dd965336a1507a', 'width': 640}, {'height': 320, 'url': 'https://i.scdn.co/image/ab676161000051745da36f8b98dd965336a1507a', 'width': 320}, {'height': 160, 'url': 'https://i.scdn.co/image/ab6761610000f1785da36f8b98dd965336a1507a', 'width': 160}], 'name': 'blink-182', 'popularity': 79, 'type': 'artist', 'uri': 'spotify:artist:6FBDaR13swtiWwGhX1WQsP'}
selected_songs = songs.get_random_songs([blink_182, pax_217], 5, True, {})

idx = 0
for song in selected_songs:
    if song is not None:
        print(idx, song["artists"][0]["name"], song["name"])
        idx += 1