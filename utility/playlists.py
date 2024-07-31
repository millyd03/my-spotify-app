from definition.day_intros import DayIntros
from model.api.create_daily_drive_playlist_request import SelectedPodcast
from utility.podcasts import Podcasts
from utility.songs import Songs
from datetime import datetime


class Playlists:

    def __init__(self, sp):
        self.sp = sp

    def get_my_playlists(self):
        all_results = []
        page_size = 50

        response = self.sp.current_user_playlists(page_size, 0)
        all_results.extend(response["items"])
        total_count = response["total"]
        offset = page_size
        if total_count > page_size:
            for i in range(total_count):
                response = self.sp.current_user_playlists(page_size, offset)

                all_results.extend(response["items"])

                next_page_url = response.get('next', None)
                if not next_page_url:
                    break

                offset += page_size

        return all_results

    def delete_playlist(self, playlist_id):
        self.sp.current_user_unfollow_playlist(playlist_id)

    def create_playlist(self, name):
        current_user = self.sp.me()
        todays_playlist = self.sp.user_playlist_create(current_user["id"], name)

        return todays_playlist["id"]

    def add_to_playlist(self, playlist_id, tracks, position=None):
        self.sp.playlist_add_items(playlist_id, tracks, position)

    def create_daily_drive_playlist(self, number_of_songs, songs_between, artists, selected_podcasts, cache_file, clean=True, weekday_name="Today", debug=False):
        manual = False

        if weekday_name != "Today":
            manual = True
        else:
            today = datetime.today()
            weekday_name = today.strftime("%A")

        playlists = Playlists(self.sp)
        my_playlists = playlists.get_my_playlists()

        # Start with 50 songs
        for idx, playlist in enumerate(my_playlists):
            if "name" in playlist and playlist["name"] == f"My {weekday_name} Drive":
                playlists.delete_playlist(playlist["id"])
                break

        playlist_id = playlists.create_playlist(f"My {weekday_name} Drive")

        songs = Songs(self.sp)
        playlist_songs = songs.get_random_songs(artists, number_of_songs, cache_file, clean, artist_counts={})

        tracks = []
        idx = 0
        for song in playlist_songs:
            if song is not None:
                tracks.append("spotify:track:" + song["id"])
                print(idx, song["artists"][0]["name"], song["name"])
                idx += 1

        if not debug:
            playlists.add_to_playlist(playlist_id, tracks)
        day_intro_enum = getattr(DayIntros, weekday_name.upper(), None)
        if day_intro_enum is None:
            day_intro_track = "6S1kSZwTOv93ZmClI5tekm"
        else:
            day_intro_track = day_intro_enum.value
        if day_intro_track is not None and len(day_intro_track) > 0:
            if not debug:
                playlists.add_to_playlist(playlist_id, ["spotify:track:" + day_intro_track], 0)

        podcasts = Podcasts(self.sp)

        location = 1
        for idx, podcast in enumerate(selected_podcasts):

            if isinstance(podcast, SelectedPodcast):
                podcast = dict(podcast.__dict__)

            if podcast["most_recent"]:
                if manual:
                    todays_show = podcasts.get_podcast_from_past_weeks_day(podcast["id"], weekday_name)
                else:
                    todays_show = podcasts.get_podcast_recent_episodes(podcast["id"], 1)
                if todays_show[0]["duration_ms"] > 1800000:
                    chunks = int(todays_show[0]["duration_ms"] / 1800000)
                    for n in range(chunks):
                        if not debug:
                            playlists.add_to_playlist(playlist_id, ["spotify:episode:" + todays_show[0]["id"]],
                                                      location)
                        print(location, podcast["name"], todays_show[0]["name"])
                        location += songs_between + 1
                else:
                    if not debug:
                        playlists.add_to_playlist(playlist_id, ["spotify:episode:" + todays_show[0]["id"]], location)
                    print(location, podcast["name"], todays_show[0]["name"])
                    location += songs_between + 1
            else:
                todays_show = podcasts.get_podcast_oldest_unplayed_episode(podcast["id"])
                if todays_show is not None:
                    if not debug:
                        playlists.add_to_playlist(playlist_id, ["spotify:episode:" + todays_show["id"]], location)
                    print(location, podcast["name"], todays_show["name"])
                    location += songs_between + 1
