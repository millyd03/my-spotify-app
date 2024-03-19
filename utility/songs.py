from model.api.create_daily_drive_playlist_request import SelectedArtist
from utility import util


def get_random_song(songs, artist_name):
    max_val = len(songs["tracks"])

    if max_val <= 0:
        print("Bad artist:", artist_name, max_val)
        return None

    random_song_idx = util.get_random_int(0, max_val - 1)

    return songs["tracks"][random_song_idx]


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

    def get_random_songs(self, artists, n, clean=True):
        random_songs = []

        for i in range(n):
            random_artist = get_random_artist(artists)

            if isinstance(random_artist, SelectedArtist):
                random_artist = dict(random_artist.__dict__)

            artists_top_songs = self.get_artists_top_songs(random_artist["id"])
            selected_song = get_random_song(artists_top_songs, random_artist["name"])

            while selected_song is None or (selected_song["explicit"] and clean) or selected_song["is_playable"] is False:
                if selected_song is None:
                    random_artist = get_random_artist(artists)
                    artists_top_songs = self.get_artists_top_songs(random_artist["id"])
                selected_song = get_random_song(artists_top_songs, random_artist["name"])

            random_songs.append(selected_song)

        return random_songs
