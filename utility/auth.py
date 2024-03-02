import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth


class Auth:
    def __init__(self, client_id, client_secret, redirect_uri=""):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

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
            auth_manager = SpotifyClientCredentials(self.client_id, self.client_secret)
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
                                    scope="user-read-private user-read-email user-follow-read playlist-modify-public playlist-modify-private user-read-playback-position")

        try:
            sp = spotipy.Spotify(auth_manager=auth_manager)
            return sp
        except spotipy.SpotifyException as e:
            raise Exception(f"Error creating Spotify connection: {e}") from e
