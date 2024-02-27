class Artists:

    def __init__(self, sp):
        self.sp = sp

    def get_my_followed_artists(self):
        all_results = []
        last_artist_id = None

        while True:
            response = self.sp.current_user_followed_artists(50, last_artist_id)

            if not response:  # Handle empty response
                break

            all_results.extend(response["artists"]["items"])

            next_page_url = response["artists"].get('next', None)
            if not next_page_url:
                break

            last_artist_id = all_results[-1]["id"]

        return all_results

    def get_artist(self, artist_id):
        return self.sp.artist(artist_id)
