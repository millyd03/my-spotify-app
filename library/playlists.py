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
