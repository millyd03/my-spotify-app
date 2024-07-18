from utility.artists import Artists
from utility.auth import Auth
import yaml

from utility.songs import get_random_artist

config_file = "../config/config.yml"

with open(config_file, "r") as file:
    config_data = yaml.safe_load(file)

auth = Auth(config_data["client_id"], config_data["client_secret"], config_data["redirect_uri"])
sp = auth.get_spotify_connection_with_authorization_code()
user = sp.current_user()
artists = Artists(sp)
followed_artists = artists.get_my_followed_artists()

for idx, artist in enumerate(followed_artists):
    print(artist)

artist_genres = artists.get_followed_genres()

# Print the unique genres and their counts
for genre, genre_artists in artist_genres.items():
    print(f"Genre: {genre}, Count: {len(genre_artists)}")

random_artist = get_random_artist(followed_artists)
print(random_artist)

favorite_artists = ['3jOstUTkEu2JkjvRdBA5Gu',  #Weezer
                    '7oPftvlwr6VrsViSDV7fJY',  #Green Day
                    '4ghjRm4M2vChDfTUycx0Ce',  #New Found Glory
                    '6FBDaR13swtiWwGhX1WQsP',  #blink-182
                    '3Ayl7mCk0nScecqOzvNp6s',  #Jimmy Eat World
                    '54Bjxn26WsjfslQbNVtSCm',  #The Get Up Kids
                    '0eW6yRE8ePadhUe1Numam9',  #Sherwood
                    '6VLj1qK2dmR3P2yMNTSn2Y',  #Bleach
                    '1sxRcl7G7tpQvuQkMyAWau',  #Slick Shoes
                    '1Enp9WKfk0aI9CFi2YGBq7',  #Further Seems Forever
                    '3nJWBJvK7uGvfp4iZh9CkN',  #Relient K
                    '0qT79UgT5tY4yudH9VfsdT',  #Sum 41
                    '3lqHnJKd9fNQEV7Ewcd0Ge',  #Dogwood
                    '0FguhfqSypXh6FuYJHkI6w',  #Children 18:3
                    '7zn1qF9KcBCxwj2Rpn4fAp',  #Over It
                    '1aEYCT7t18aM3VvM6y8oVR',  #Alkaline Trio
                    '3zxKH0qp3nBCuPZCZT5Vaf'  #Yellowcard
                    ]

random_artist = get_random_artist(favorite_artists)
print(random_artist)