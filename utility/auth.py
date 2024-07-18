import spotipy
import yaml
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

from utility.user_cache_handler import UserCacheHandler


def connect_with_config():
    config_file = "../config/config.yml"

    with open(config_file, "r") as file:
        config_data = yaml.safe_load(file)

    auth = Auth(config_data["client_id"], config_data["client_secret"], config_data["redirect_uri"])
    return auth.get_spotify_connection_with_authorization_code()

class Auth:
    def __init__(self, client_id, client_secret, redirect_uri=""):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.cache_path = "../cache/user_tokens"

    def get_spotify_connection_with_credentials(self):
        """
        Establishes a Spotify connection using the provided credentials and returns the spotipy.Spotify object.

        Returns:
            spotipy.Spotify: The spotipy.Spotify object for interacting with the Spotify API.

        Raises:
            ValueError: If any of the required credentials are missing.
            spotipy.SpotifyException: If there's an error creating the Spotify object.
        """

        if not self.client_id or not self.client_secret:
            raise ValueError("Both client_id and client_secret are required.")

        try:
            auth_manager = SpotifyClientCredentials(self.client_id, self.client_secret,
                                                    cache_handler=UserCacheHandler(self.cache_path, self.client_id))
            sp = spotipy.Spotify(auth_manager=auth_manager)
            return sp
        except spotipy.SpotifyException as e:
            raise Exception(f"Error creating Spotify connection: {e}") from e

    def get_spotify_connection_with_authorization_code(self):
        """
        Establishes a Spotify connection using the Authorization Code flow and returns the spotipy.Spotify object.

        Requires a user authorization step beforehand to obtain an access token.

        Raises:
            ValueError: If any of the required credentials or redirect URI are missing.
            spotipy.SpotifyException: If there's an error creating the Spotify object.
        """

        if not self.client_id or not self.client_secret or not self.redirect_uri:
            raise ValueError("All credentials and redirect URI are required.")

        auth_manager = SpotifyOAuth(client_id=self.client_id,
                                    client_secret=self.client_secret,
                                    redirect_uri=self.redirect_uri,
                                    scope="user-read-private user-read-email user-library-read user-follow-read playlist-modify-public playlist-modify-private user-read-playback-position",
                                    cache_handler=UserCacheHandler(self.cache_path, self.client_id))

        try:
            sp = spotipy.Spotify(auth_manager=auth_manager)
            return sp
        except spotipy.SpotifyException as e:
            raise Exception(f"Error creating Spotify connection: {e}") from e
