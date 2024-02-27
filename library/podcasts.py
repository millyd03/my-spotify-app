import calendar
from datetime import date, timedelta


class Podcasts:

    def __init__(self, sp):
        self.sp = sp

    def get_podcast_recent_episodes(self, podcast_id, limit=5, market="US"):
        response = self.sp.show_episodes(podcast_id, limit, 0, market)
        return response["items"]

    def get_my_followed_podcasts(self, market="US"):
        all_results = []
        page_size = 50

        response = self.sp.current_user_saved_shows(20, 0, market)
        all_results.extend(response["items"])
        total_count = response["total"]
        offset = page_size
        if total_count > page_size:
            for i in range(total_count):
                response = self.sp.current_user_saved_shows(page_size, offset, market)

                all_results.extend(response["items"])

                next_page_url = response.get('next', None)
                if not next_page_url:
                    break

                offset += page_size

        return all_results

    def get_podcast_from_past_weeks_day(self, podcast_id, weekday_name, limit=10, market="US"):
        response = self.sp.show_episodes(podcast_id, limit, 0, market)
        results = []

        today = date.today()
        calendar_enum_day = getattr(calendar, weekday_name.upper(), None)
        offset_days = (today.weekday() - calendar_enum_day) % 7
        past_date = today - timedelta(days=offset_days)
        formatted_date = past_date.strftime("%Y-%m-%d")

        for i in range(len(response["items"])):
            if response["items"][i]["release_date"] == formatted_date:
                results.append(response["items"][i])

        return results
