from utility.auth import Auth

auth = Auth("f5ebeabfb2f544e5a7d957c4d9e6467d", "ec1ea8302bb342a9845f780e9d40a77f", "http://localhost:8888/callback")
sp = auth.get_spotify_connection_with_authorization_code()

user_info = sp.current_user()
print(user_info["id"], user_info["display_name"])
