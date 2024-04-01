from spotipy.oauth2 import CacheHandler
from diskcache import Cache  # Example using diskcache


class UserCacheHandler(CacheHandler):

    def __init__(self, cache_path, client_id):
        self.cache = Cache(cache_path)
        self.client_id = client_id

    def get(self, key):
        # Implement logic to retrieve token data from cache based on user ID (key)
        user_id, token_type = key.split(":")
        user_data = self.cache.get(user_id)
        if user_data and token_type in user_data:
            return user_data[token_type]
        return None

    def set(self, key, value):
        # Implement logic to store token data in cache for a specific user ID (key)
        user_id, token_type = key.split(":")
        user_data = self.cache.get(user_id, {})
        user_data[token_type] = value
        self.cache.set(user_id, user_data)

    def get_cached_token(self):
        # Implement logic to retrieve cached token data (access token and refresh token) from your cache
        cached_data = self.cache.get(self.client_id)  # Replace with your cache key
        if cached_data:
            return cached_data
        return None  # Return None if no cached token found

    def save_token_to_cache(self, token_info):
        # Implement logic to store token information (access token and refresh token) in your cache
        self.cache.set(self.client_id, token_info)  # Replace with your cache key
