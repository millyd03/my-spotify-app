import yaml
from fastapi import FastAPI, Header

from model.api.artist import Artist
from model.api.create_daily_drive_playlist_request import CreateDailyDrivePlaylistRequest
from model.api.podcast import Podcast
from model.api.user import User
from utility.artists import Artists
from utility.auth import Auth
from utility.playlists import Playlists
from utility.podcasts import Podcasts

# Create an instance of the MySpotifyApp class
app = FastAPI()


def connect(client_id=None, client_secret=None, redirect_uri="http://localhost:8888/callback"):
    if client_id is None:
        config_file = "config/config.yml"

        with open(config_file, "r") as file:
            config_data = yaml.safe_load(file)
        client_id = config_data["client_id"]
        client_secret = config_data["client_secret"]

    auth = Auth(client_id, client_secret, redirect_uri)
    return auth.get_spotify_connection_with_authorization_code()


@app.get("/")
async def root(self):
    return {"message": "Hello World from FastAPI!"}


@app.get("/artists")
def get_followed_artists(client_id: str = Header(None, description="Spotify Client ID"),
                         client_secret: str = Header(None, description="Spotify Client Secret"),
                         redirect_uri: str = Header("http://localhost:8888/callback", description="Spotify Redirect URI")):
    sp = connect(client_id, client_secret, redirect_uri)
    artists_response = []
    artists = Artists(sp)
    followed_artists = artists.get_my_followed_artists()
    for idx, artist in enumerate(followed_artists):
        artists_response.append(Artist(id=artist["id"], name=artist["name"]))

    return artists_response


@app.get("/podcasts")
def get_followed_podcasts(client_id: str = Header(None, description="Spotify Client ID"),
                          client_secret: str = Header(None, description="Spotify Client Secret"),
                          redirect_uri: str = Header("http://localhost:8888/callback", description="Spotify Redirect URI")):
    sp = connect(client_id, client_secret, redirect_uri)
    podcasts_response = []
    podcasts = Podcasts(sp)
    followed_podcasts = podcasts.get_my_followed_podcasts()
    for idx, podcast in enumerate(followed_podcasts):
        podcasts_response.append(Podcast(id=podcast["show"]["id"], name=podcast["show"]["name"]))

    return podcasts_response


@app.post("/create_daily_drive_playlist")
def create_daily_drive_playlist(request: CreateDailyDrivePlaylistRequest,
                                client_id: str = Header(None, description="Spotify Client ID"),
                                client_secret: str = Header(None, description="Spotify Client Secret"),
                                redirect_uri: str = Header("http://localhost:8888/callback", description="Spotify Redirect URI")):
    sp = connect(client_id, client_secret, redirect_uri)
    cache_file = "../cache/artist_tracks_cache"

    playlists = Playlists(sp)
    playlists.create_daily_drive_playlist(request.number_of_songs, request.songs_between, request.artists,
                                          request.podcasts, cache_file, request.clean, request.day, request.debug)

    return {"message": "Playlist created successfully!"}


@app.get("/user")
def get_user(client_id: str = Header(None, description="Spotify Client ID"),
             client_secret: str = Header(None, description="Spotify Client Secret"),
             redirect_uri: str = Header("http://localhost:8888/callback", description="Spotify Redirect URI")):
    sp = connect(client_id, client_secret, redirect_uri)

    user_info = sp.current_user()
    user = User(id=user_info["id"], name=user_info["display_name"])

    return user


# Run the application using uvicorn (optional, can be called directly from the class)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.app:app", host="0.0.0.0", port=8000)
