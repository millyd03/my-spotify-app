from definition.artist_tiers import ArtistTiers
from model.api.create_daily_drive_playlist_request import SelectedArtist
from utility import util


def get_random_song(songs, artist, clean, artist_counts=None, attempts=0):
    max_val = len(songs["tracks"])

    if max_val <= 0:
        print("Bad artist:", artist["name"], max_val)
        return None

    random_song_idx = util.get_random_int(0, max_val - 1)

    if artist_counts is not None:
        under_limit = add_song_to_playlist_if_artist_under_limit(artist, artist_counts)
        if under_limit is True:
            selected_song = songs["tracks"][random_song_idx]
        else:
            print("Artist exceeded limit:", artist["name"], under_limit)
            return None
    else:
        selected_song = songs["tracks"][random_song_idx]

    if (selected_song["explicit"] and clean) or selected_song["is_playable"] is False:
        if attempts >= 5:
            return get_random_song(songs, artist, False)
        else:
            return get_random_song(songs, artist, clean, attempts=attempts + 1)
    else:
        return selected_song


def add_song_to_playlist_if_artist_under_limit(artist, artist_counts):
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

    # Get the current count for the artist (default 0 if not present)
    artist_count = artist_counts.get(artist["id"], 0)

    # Loop through tier thresholds and check conditions
    for idx, tier_limit in enumerate(tier_thresholds):
        if artist["followers"]["total"] < tier_limit:
            if artist_count < idx + 1:  # Adjust for 0-based indexing of tiers
                return True
            else:
                return artist_counts[artist["id"]]

def get_random_artist(artists):
    max_val = len(artists)

    random_artist_idx = util.get_random_int(0, max_val - 1)

    return artists[random_artist_idx]


class Songs:
    def __init__(self, sp):
        self.sp = sp

    def get_artists_top_songs(self, artist_id):
        return self.sp.artist_top_tracks(artist_id)

    def get_all_artists_songs(self, artist_id):
        return self.sp.artist_top_tracks(artist_id)

    def get_random_songs(self, artists, n, clean=True, artist_counts=None, favorite_artists=None):
        random_songs = []

        for i in range(n):
            random_artist = get_random_artist(artists)

            if isinstance(random_artist, SelectedArtist):
                random_artist = dict(random_artist.__dict__)

            artists_top_songs = self.get_artists_top_songs(random_artist["id"])
            selected_song = get_random_song(artists_top_songs, random_artist, clean, artist_counts)

            emergency_break = 0
            while selected_song is None:
                if favorite_artists is not None:
                    random_artist = get_random_artist(favorite_artists)
                    artists_top_songs = self.get_artists_top_songs(random_artist["id"])
                    print("Replacing with " + random_artist["name"])
                else:
                    emergency_break += 1
                    random_artist = get_random_artist(artists)
                    artists_top_songs = self.get_artists_top_songs(random_artist["id"])

                if emergency_break >= 10:
                    selected_song = get_random_song(artists_top_songs, random_artist, clean, None)
                else:
                    selected_song = get_random_song(artists_top_songs, random_artist, clean, artist_counts)

            if artist_counts is not None:
                artist_count = artist_counts.get(random_artist["id"], 0)
                artist_counts[random_artist["id"]] = artist_count + 1
            random_songs.append(selected_song)

        return random_songs
