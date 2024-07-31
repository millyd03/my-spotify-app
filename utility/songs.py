import json
import os

from definition.artist_tiers import ArtistTiers
from definition.song_filters import SongFilters
from model.api.create_daily_drive_playlist_request import SelectedArtist
from utility import util
from utility.artists import Artists
from utility.auth import connect_with_config
from utility.util import check_is_between_dates
from utility.spotipy_facade import search
from utility.spotipy_facade import artist_top_tracks


def get_random_song(songs, artist, clean, artist_counts=None, attempts=0, favorite_artists=None):
    max_val = len(songs)

    if max_val <= 0:
        print("Bad artist:", artist["name"], max_val)
        return None

    random_song_idx = util.get_random_int(0, max_val - 1)

    if artist_counts is not None:
        under_limit = add_song_to_playlist_if_artist_under_limit(artist, artist_counts, favorite_artists)
        if under_limit is True:
            selected_song = songs[random_song_idx]
        else:
            print("Artist exceeded limit:", artist["name"], under_limit)
            return None
    else:
        selected_song = songs[random_song_idx]

    if selected_song["explicit"] and clean:
        if attempts >= 5:
            return get_random_song(songs, artist, False, favorite_artists=favorite_artists)
        else:
            return get_random_song(songs, artist, clean, attempts=attempts + 1, favorite_artists=favorite_artists)
    else:
        return selected_song


def add_song_to_playlist_if_artist_under_limit(artist, artist_counts, favorite_artists=None):
    tier_thresholds = [ArtistTiers.TIER_1.value, ArtistTiers.TIER_2.value, ArtistTiers.TIER_3.value,
                       ArtistTiers.TIER_4.value, ArtistTiers.TIER_5.value, ArtistTiers.TIER_6.value]

    """
  This method checks if the artist can be added to a playlist based on a limit.

  Args:
      song: The song title (string).
      artist: The artist name (string).
      artist_counts: A hashmap containing artist names as keys and their song counts as values (integer).

  Returns:
      True if the artist can be added (count less than 5), False otherwise.
  """

    if favorite_artists is not None and artist["id"] in favorite_artists:
        return True

    # Get the current count for the artist (default 0 if not present)
    artist_count = artist_counts.get(artist["id"], 0)

    # Loop through tier thresholds and check conditions
    for idx, tier_limit in enumerate(tier_thresholds):
        if artist["followers"]["total"] < tier_limit:
            if artist_count < idx + 1:  # Adjust for 0-based indexing of tiers
                return True
            else:
                return artist_counts[artist["id"]]


def get_random_artist(artists_list):
    max_val = len(artists_list)

    random_artist_idx = util.get_random_int(0, max_val - 1)

    if isinstance(artists_list[random_artist_idx], str):
        sp = connect_with_config()
        artists = Artists(sp)
        return artists.get_artist(artists_list[random_artist_idx])
    else:
        return artists_list[random_artist_idx]


class Songs:
    def __init__(self, sp):
        self.sp = sp

    def get_artists_top_songs(self, artist_id):
        return artist_top_tracks(self.sp, artist_id)["tracks"]

    def get_all_artists_songs(self, artist_name, cache_file, limit=50, start_date=None, end_date=None):
        """Gets all songs by an artist sorted by release date (ascending order).

        Args:
            artist_name: The name of the artist.
            cache_file:
            limit: The number of results per page (default: 50, maximum: 50).
            start_date:
            end_date:

        Returns:
            A list of dictionaries representing all songs sorted by release date with keys 'name', 'release_date'.
        """

        cache_key = f"all_artist_tracks:{artist_name}"

        # Check if the data is in the cache
        if os.path.exists(cache_file):
            # Load the cache from the file
            with open(cache_file, 'r') as f:
                cache = json.load(f)
        else:
            cache = {}

        # Check if the data is in the cache
        if cache is not {} and cache_key in cache:
            print("Cache hit! " + cache_key)
            all_songs = cache[cache_key]
        else:
            # Initialize variables
            all_songs = []
            offset = 0

            # Loop to retrieve results from multiple pages
            while True:
                # Perform search with limit and offset
                results = search(self.sp, q=artist_name, limit=limit, offset=offset)

                # Extract artists from the current page
                songs = results['tracks']['items']
                all_songs.extend(songs)

                # Check for next page (indicated by 'next' key in response)
                if not results['tracks']['next']:
                    break

                # Update offset for the next page
                offset += limit

            # Cache the results
            cache[cache_key] = all_songs

            # Save the cache to the file
            with open(cache_file, 'w') as f:
                json.dump(cache, f)

            # Loop through the list with index
        for index in reversed(range(len(all_songs))):
            song = all_songs[index]

            # Extract artist names from the track
            artists = [artist['name'] for artist in song['artists']]

            # Check if the artist name is present in the list (case-sensitive)
            if artist_name not in artists or (
                    start_date is not None and not check_is_between_dates(song['album']['release_date'], start_date,
                                                                          end_date)):
                del all_songs[index]

        # Return the sorted list of songs
        return all_songs

    def get_top_old_songs(self, artist_name, cache_file):
        """Gets the top 20 most popular songs by an artist released in the last 5 years.

        Args:
            artist_name: The name of the artist.
            cache_file:

        Returns:
            A list of dictionaries representing the top 20 songs with keys 'name', 'release_date', and 'popularity'.
        """

        # Get all artist's releases
        filtered_songs = self.get_all_artists_songs(artist_name, cache_file, start_date='1990-01-01', end_date='2010-01-01')

        # Sort songs by popularity (descending order)
        filtered_songs.sort(key=lambda song: song['popularity'], reverse=True)

        # Return the top 20 songs
        return filtered_songs[:20]

    def get_top_new_songs(self, artist_name, cache):
        """Gets the top 20 most popular songs by an artist released in the last 5 years.

        Args:
            artist_name: The name of the artist.

        Returns:
            A list of dictionaries representing the top 20 songs with keys 'name', 'release_date', and 'popularity'.
        """

        # Get all artist's releases
        filtered_songs = self.get_all_artists_songs(artist_name, cache, start_date='2020-01-01', end_date='2025-01-01')

        # Sort songs by popularity (descending order)
        filtered_songs.sort(key=lambda song: song['popularity'], reverse=True)

        # Return the top 20 songs
        return filtered_songs[:20]

    def get_random_songs(self, artists, n, cache_file, clean=True, artist_counts=None, favorite_artists=None, song_filter=None):
        random_songs = []

        for i in range(n):
            random_artist = get_random_artist(artists)

            if isinstance(random_artist, SelectedArtist):
                random_artist = dict(random_artist.__dict__)

            if song_filter is SongFilters.WILDCARD:
                song_list = self.get_all_artists_songs(random_artist["name"], cache_file)
            elif song_filter is SongFilters.THROWBACK:
                song_list = self.get_top_old_songs(random_artist["name"], cache_file)
            elif song_filter is SongFilters.FRESH:
                song_list = self.get_top_new_songs(random_artist["name"], cache_file)
            else:
                song_list = self.get_artists_top_songs(random_artist["id"])
            selected_song = get_random_song(song_list, random_artist, clean, artist_counts, favorite_artists=favorite_artists)

            emergency_break = 0
            while selected_song is None:
                if favorite_artists is not None:
                    random_artist = get_random_artist(favorite_artists)
                    song_list = self.get_artists_top_songs(random_artist["id"])
                    print("Replacing with " + random_artist["name"])
                else:
                    emergency_break += 1
                    random_artist = get_random_artist(artists)
                    song_list = self.get_artists_top_songs(random_artist["id"])

                if emergency_break >= 10:
                    selected_song = get_random_song(song_list, random_artist, clean, None, favorite_artists=favorite_artists)
                else:
                    selected_song = get_random_song(song_list, random_artist, clean, artist_counts, favorite_artists=favorite_artists)

            if artist_counts is not None:
                artist_count = artist_counts.get(random_artist["id"], 0)
                artist_counts[random_artist["id"]] = artist_count + 1
            random_songs.append(selected_song)

        return random_songs
