import spotipy

from utility.auth import connect_with_config


def search(sp, q, limit=10, offset=0, type="track", market=None):
    """
    Retries the Spotify search with exponential backoff in case of timeouts.

    Args:
        sp: A Spotipy client instance.
        query: The search query.
        limit: The maximum number of items to return.
        offset: The index of the first item to return.
        type: The type of item to search for.
        market: An optional ISO 3166-1 alpha-2 country code or a string of the form 'XX-YY'.

    Returns:
        The search results or None if all retries fail.
    """

    try:
        results = sp.search(q=q, limit=limit, offset=offset, type=type, market=market)
        return results
    except spotipy.exceptions.SpotifyException as e:
        if e.http_status in [401, 429]:  # Unauthorized or rate limit exceeded
            # Handle session timeout or rate limit by re-authenticating or waiting
            print("Spotify authentication error. Retrying...")
            sp = connect_with_config()
            results = sp.search(q=q, limit=limit, offset=offset, type=type, market=market)
            return results
        else:
            raise  # Re-raise other exceptions


def current_user(sp):
    """
    Retries the Spotify search with exponential backoff in case of timeouts.

    Args:
        sp: A Spotipy client instance.

    Returns:
        The search results or None if all retries fail.
    """

    try:
        results = sp.current_user()
        return results
    except spotipy.exceptions.SpotifyException as e:
        if e.http_status in [401, 429]:  # Unauthorized or rate limit exceeded
            # Handle session timeout or rate limit by re-authenticating or waiting
            print("Spotify authentication error. Retrying...")
            sp = connect_with_config()
            results = sp.current_user()
            return results
        else:
            raise  # Re-raise other exceptions


def artist_top_tracks(sp, artist_id):
    """
    Retries the Spotify search with exponential backoff in case of timeouts.

    Args:
        sp: A Spotipy client instance.

    Returns:
        The search results or None if all retries fail.
    """

    try:
        results = sp.artist_top_tracks(artist_id)
        return results
    except spotipy.exceptions.SpotifyException as e:
        if e.http_status in [401, 429]:  # Unauthorized or rate limit exceeded
            # Handle session timeout or rate limit by re-authenticating or waiting
            print("Spotify authentication error. Retrying...")
            sp = connect_with_config()
            results = artist_top_tracks(artist_id)
            return results
        else:
            raise  # Re-raise other exceptions