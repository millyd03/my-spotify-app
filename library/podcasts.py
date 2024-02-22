class Podcasts:

    def __init__(self, sp):
        self.sp = sp

    def get_podcast_recent_episodes(self, show_id, limit=5, market="US"):
        return self.sp.show_episodes(show_id, limit, 0, market)

    def get_my_followed_podcasts(self, market="US"):
        all_results = []

        response = self.sp.current_user_saved_shows(20, 0, market)
        all_results.extend(response["items"])
        total_count = response["total"]
        offset = 20
        if total_count > 20:
            for i in range(total_count):
                response = self.sp.current_user_saved_shows(20, offset, market)

                all_results.extend(response["items"])

                next_page_url = response.get('next', None)
                if not next_page_url:
                    break

                offset += 20

        return all_results
