import yaml

from utility.auth import Auth
from utility.songs import Songs

config_file = "../config/config.yml"

with open(config_file, "r") as file:
    config_data = yaml.safe_load(file)

auth = Auth(config_data["client_id"], config_data["client_secret"], config_data["redirect_uri"])
sp = auth.get_spotify_connection_with_authorization_code()

favorite_artists = [{'external_urls': {'spotify': 'https://open.spotify.com/artist/3jOstUTkEu2JkjvRdBA5Gu'},
                     'followers': {'href': None, 'total': 3529166},
                     'genres': ['alternative rock', 'modern power pop', 'modern rock', 'permanent wave', 'rock'],
                     'href': 'https://api.spotify.com/v1/artists/3jOstUTkEu2JkjvRdBA5Gu',
                     'id': '3jOstUTkEu2JkjvRdBA5Gu', 'images': [
        {'height': 640, 'url': 'https://i.scdn.co/image/ab6761610000e5eb3cd35451daa1b690cfbbb2d4', 'width': 640},
        {'height': 320, 'url': 'https://i.scdn.co/image/ab676161000051743cd35451daa1b690cfbbb2d4', 'width': 320},
        {'height': 160, 'url': 'https://i.scdn.co/image/ab6761610000f1783cd35451daa1b690cfbbb2d4', 'width': 160}],
                     'name': 'Weezer', 'popularity': 71, 'type': 'artist',
                     'uri': 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'},
                    {'external_urls': {'spotify': 'https://open.spotify.com/artist/7oPftvlwr6VrsViSDV7fJY'},
                     'followers': {'href': None, 'total': 14857432},
                     'genres': ['modern rock', 'permanent wave', 'punk', 'rock'],
                     'href': 'https://api.spotify.com/v1/artists/7oPftvlwr6VrsViSDV7fJY',
                     'id': '7oPftvlwr6VrsViSDV7fJY', 'images': [
                        {'height': 640, 'url': 'https://i.scdn.co/image/ab6761610000e5eb6ff0cd5ef2ecf733804984bb',
                         'width': 640},
                        {'height': 320, 'url': 'https://i.scdn.co/image/ab676161000051746ff0cd5ef2ecf733804984bb',
                         'width': 320},
                        {'height': 160, 'url': 'https://i.scdn.co/image/ab6761610000f1786ff0cd5ef2ecf733804984bb',
                         'width': 160}], 'name': 'Green Day', 'popularity': 77, 'type': 'artist',
                     'uri': 'spotify:artist:7oPftvlwr6VrsViSDV7fJY'},
                    {'external_urls': {'spotify': 'https://open.spotify.com/artist/4ghjRm4M2vChDfTUycx0Ce'},
                     'followers': {'href': None, 'total': 826949}, 'genres': ['easycore', 'neon pop punk', 'pop punk'],
                     'href': 'https://api.spotify.com/v1/artists/4ghjRm4M2vChDfTUycx0Ce',
                     'id': '4ghjRm4M2vChDfTUycx0Ce', 'images': [
                        {'height': 640, 'url': 'https://i.scdn.co/image/ab6761610000e5eb700da92fd7837bba20d58713',
                         'width': 640},
                        {'height': 320, 'url': 'https://i.scdn.co/image/ab67616100005174700da92fd7837bba20d58713',
                         'width': 320},
                        {'height': 160, 'url': 'https://i.scdn.co/image/ab6761610000f178700da92fd7837bba20d58713',
                         'width': 160}], 'name': 'New Found Glory', 'popularity': 54, 'type': 'artist',
                     'uri': 'spotify:artist:4ghjRm4M2vChDfTUycx0Ce'},
                    {'external_urls': {'spotify': 'https://open.spotify.com/artist/6FBDaR13swtiWwGhX1WQsP'},
                     'followers': {'href': None, 'total': 8194577},
                     'genres': ['alternative metal', 'modern rock', 'pop punk', 'punk', 'rock', 'socal pop punk'],
                     'href': 'https://api.spotify.com/v1/artists/6FBDaR13swtiWwGhX1WQsP',
                     'id': '6FBDaR13swtiWwGhX1WQsP', 'images': [
                        {'height': 640, 'url': 'https://i.scdn.co/image/ab6761610000e5eb5da36f8b98dd965336a1507a',
                         'width': 640},
                        {'height': 320, 'url': 'https://i.scdn.co/image/ab676161000051745da36f8b98dd965336a1507a',
                         'width': 320},
                        {'height': 160, 'url': 'https://i.scdn.co/image/ab6761610000f1785da36f8b98dd965336a1507a',
                         'width': 160}], 'name': 'blink-182', 'popularity': 75, 'type': 'artist',
                     'uri': 'spotify:artist:6FBDaR13swtiWwGhX1WQsP'},
                    {'external_urls': {'spotify': 'https://open.spotify.com/artist/3Ayl7mCk0nScecqOzvNp6s'},
                     'followers': {'href': None, 'total': 1548130},
                     'genres': ['alternative metal', 'alternative rock', 'emo', 'modern power pop', 'modern rock',
                                'neon pop punk', 'pop punk', 'pop rock', 'post-grunge', 'punk', 'rock'],
                     'href': 'https://api.spotify.com/v1/artists/3Ayl7mCk0nScecqOzvNp6s',
                     'id': '3Ayl7mCk0nScecqOzvNp6s', 'images': [
                        {'height': 640, 'url': 'https://i.scdn.co/image/ab6761610000e5eb0dc33cfd207772f8e2f6b46f',
                         'width': 640},
                        {'height': 320, 'url': 'https://i.scdn.co/image/ab676161000051740dc33cfd207772f8e2f6b46f',
                         'width': 320},
                        {'height': 160, 'url': 'https://i.scdn.co/image/ab6761610000f1780dc33cfd207772f8e2f6b46f',
                         'width': 160}], 'name': 'Jimmy Eat World', 'popularity': 66, 'type': 'artist',
                     'uri': 'spotify:artist:3Ayl7mCk0nScecqOzvNp6s'},
                    {'external_urls': {'spotify': 'https://open.spotify.com/artist/54Bjxn26WsjfslQbNVtSCm'},
                     'followers': {'href': None, 'total': 140278}, 'genres': ['emo', 'kc indie', 'midwest emo'],
                     'href': 'https://api.spotify.com/v1/artists/54Bjxn26WsjfslQbNVtSCm',
                     'id': '54Bjxn26WsjfslQbNVtSCm', 'images': [
                        {'height': 640, 'url': 'https://i.scdn.co/image/ab6761610000e5eb999da14c4a6ab491b890156e',
                         'width': 640},
                        {'height': 320, 'url': 'https://i.scdn.co/image/ab67616100005174999da14c4a6ab491b890156e',
                         'width': 320},
                        {'height': 160, 'url': 'https://i.scdn.co/image/ab6761610000f178999da14c4a6ab491b890156e',
                         'width': 160}], 'name': 'The Get Up Kids', 'popularity': 39, 'type': 'artist',
                     'uri': 'spotify:artist:54Bjxn26WsjfslQbNVtSCm'},
                    {'external_urls': {'spotify': 'https://open.spotify.com/artist/0eW6yRE8ePadhUe1Numam9'},
                     'followers': {'href': None, 'total': 23183}, 'genres': ['alternative pop rock', 'neon pop punk'],
                     'href': 'https://api.spotify.com/v1/artists/0eW6yRE8ePadhUe1Numam9',
                     'id': '0eW6yRE8ePadhUe1Numam9', 'images': [
                        {'height': 640, 'url': 'https://i.scdn.co/image/ab6761610000e5eb5feba253d63e12d1daf07ee2',
                         'width': 640},
                        {'height': 320, 'url': 'https://i.scdn.co/image/ab676161000051745feba253d63e12d1daf07ee2',
                         'width': 320},
                        {'height': 160, 'url': 'https://i.scdn.co/image/ab6761610000f1785feba253d63e12d1daf07ee2',
                         'width': 160}], 'name': 'Sherwood', 'popularity': 20, 'type': 'artist',
                     'uri': 'spotify:artist:0eW6yRE8ePadhUe1Numam9'},
                    {'external_urls': {'spotify': 'https://open.spotify.com/artist/6VLj1qK2dmR3P2yMNTSn2Y'},
                     'followers': {'href': None, 'total': 3264}, 'genres': ['christian punk'],
                     'href': 'https://api.spotify.com/v1/artists/6VLj1qK2dmR3P2yMNTSn2Y',
                     'id': '6VLj1qK2dmR3P2yMNTSn2Y', 'images': [
                        {'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273aa865cb9e337134add04b932',
                         'width': 640},
                        {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02aa865cb9e337134add04b932',
                         'width': 300},
                        {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851aa865cb9e337134add04b932',
                         'width': 64}], 'name': 'Bleach', 'popularity': 17, 'type': 'artist',
                     'uri': 'spotify:artist:6VLj1qK2dmR3P2yMNTSn2Y'},
                    {'external_urls': {'spotify': 'https://open.spotify.com/artist/1sxRcl7G7tpQvuQkMyAWau'},
                     'followers': {'href': None, 'total': 25082}, 'genres': ['christian punk', 'skate punk'],
                     'href': 'https://api.spotify.com/v1/artists/1sxRcl7G7tpQvuQkMyAWau',
                     'id': '1sxRcl7G7tpQvuQkMyAWau', 'images': [
                        {'height': 640, 'url': 'https://i.scdn.co/image/ab6761610000e5eb38b3ebaf54e44bd03d14f044',
                         'width': 640},
                        {'height': 320, 'url': 'https://i.scdn.co/image/ab6761610000517438b3ebaf54e44bd03d14f044',
                         'width': 320},
                        {'height': 160, 'url': 'https://i.scdn.co/image/ab6761610000f17838b3ebaf54e44bd03d14f044',
                         'width': 160}], 'name': 'Slick Shoes', 'popularity': 25, 'type': 'artist',
                     'uri': 'spotify:artist:1sxRcl7G7tpQvuQkMyAWau'},
                    {'external_urls': {'spotify': 'https://open.spotify.com/artist/1Enp9WKfk0aI9CFi2YGBq7'},
                     'followers': {'href': None, 'total': 40623}, 'genres': ['christian punk', 'emo', 'emo punk'],
                     'href': 'https://api.spotify.com/v1/artists/1Enp9WKfk0aI9CFi2YGBq7',
                     'id': '1Enp9WKfk0aI9CFi2YGBq7', 'images': [
                        {'height': 640, 'url': 'https://i.scdn.co/image/ab6761610000e5eb4748de5d5062d256dbfd84cb',
                         'width': 640},
                        {'height': 320, 'url': 'https://i.scdn.co/image/ab676161000051744748de5d5062d256dbfd84cb',
                         'width': 320},
                        {'height': 160, 'url': 'https://i.scdn.co/image/ab6761610000f1784748de5d5062d256dbfd84cb',
                         'width': 160}], 'name': 'Further Seems Forever', 'popularity': 29, 'type': 'artist',
                     'uri': 'spotify:artist:1Enp9WKfk0aI9CFi2YGBq7'},
                    {'external_urls': {'spotify': 'https://open.spotify.com/artist/3nJWBJvK7uGvfp4iZh9CkN'},
                     'followers': {'href': None, 'total': 362191},
                     'genres': ['canadian ccm', 'christian alternative rock', 'christian punk', 'pop punk'],
                     'href': 'https://api.spotify.com/v1/artists/3nJWBJvK7uGvfp4iZh9CkN',
                     'id': '3nJWBJvK7uGvfp4iZh9CkN', 'images': [
                        {'height': 640, 'url': 'https://i.scdn.co/image/ab6761610000e5eb1e0743a3e000215916f70238',
                         'width': 640},
                        {'height': 320, 'url': 'https://i.scdn.co/image/ab676161000051741e0743a3e000215916f70238',
                         'width': 320},
                        {'height': 160, 'url': 'https://i.scdn.co/image/ab6761610000f1781e0743a3e000215916f70238',
                         'width': 160}], 'name': 'Relient K', 'popularity': 50, 'type': 'artist',
                     'uri': 'spotify:artist:3nJWBJvK7uGvfp4iZh9CkN'},
                    {'external_urls': {'spotify': 'https://open.spotify.com/artist/0qT79UgT5tY4yudH9VfsdT'},
                     'followers': {'href': None, 'total': 3823744},
                     'genres': ['alternative metal', 'canadian pop punk', 'canadian punk', 'modern rock', 'pop punk',
                                'post-grunge', 'punk', 'rock'],
                     'href': 'https://api.spotify.com/v1/artists/0qT79UgT5tY4yudH9VfsdT',
                     'id': '0qT79UgT5tY4yudH9VfsdT', 'images': [
                        {'height': 640, 'url': 'https://i.scdn.co/image/ab6761610000e5eb625af80b68ae4eb559c6c417',
                         'width': 640},
                        {'height': 320, 'url': 'https://i.scdn.co/image/ab67616100005174625af80b68ae4eb559c6c417',
                         'width': 320},
                        {'height': 160, 'url': 'https://i.scdn.co/image/ab6761610000f178625af80b68ae4eb559c6c417',
                         'width': 160}], 'name': 'Sum 41', 'popularity': 70, 'type': 'artist',
                     'uri': 'spotify:artist:0qT79UgT5tY4yudH9VfsdT'},
                    {'external_urls': {'spotify': 'https://open.spotify.com/artist/3lqHnJKd9fNQEV7Ewcd0Ge'},
                     'followers': {'href': None, 'total': 11513}, 'genres': ['christian hardcore', 'christian punk'],
                     'href': 'https://api.spotify.com/v1/artists/3lqHnJKd9fNQEV7Ewcd0Ge',
                     'id': '3lqHnJKd9fNQEV7Ewcd0Ge', 'images': [
                        {'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273979a8ef8d6193d40b0ad4dc0',
                         'width': 640},
                        {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02979a8ef8d6193d40b0ad4dc0',
                         'width': 300},
                        {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851979a8ef8d6193d40b0ad4dc0',
                         'width': 64}], 'name': 'Dogwood', 'popularity': 20, 'type': 'artist',
                     'uri': 'spotify:artist:3lqHnJKd9fNQEV7Ewcd0Ge'},
                    {'external_urls': {'spotify': 'https://open.spotify.com/artist/0FguhfqSypXh6FuYJHkI6w'},
                     'followers': {'href': None, 'total': 19733},
                     'genres': ['christian alternative rock', 'christian punk', 'christian rock'],
                     'href': 'https://api.spotify.com/v1/artists/0FguhfqSypXh6FuYJHkI6w',
                     'id': '0FguhfqSypXh6FuYJHkI6w', 'images': [
                        {'height': 640, 'url': 'https://i.scdn.co/image/ab6761610000e5eb2e0a47f29e46ac2408407c90',
                         'width': 640},
                        {'height': 320, 'url': 'https://i.scdn.co/image/ab676161000051742e0a47f29e46ac2408407c90',
                         'width': 320},
                        {'height': 160, 'url': 'https://i.scdn.co/image/ab6761610000f1782e0a47f29e46ac2408407c90',
                         'width': 160}], 'name': 'Children 18:3', 'popularity': 19, 'type': 'artist',
                     'uri': 'spotify:artist:0FguhfqSypXh6FuYJHkI6w'},
                    {'external_urls': {'spotify': 'https://open.spotify.com/artist/7zn1qF9KcBCxwj2Rpn4fAp'},
                     'followers': {'href': None, 'total': 5622}, 'genres': ['deep pop emo'],
                     'href': 'https://api.spotify.com/v1/artists/7zn1qF9KcBCxwj2Rpn4fAp',
                     'id': '7zn1qF9KcBCxwj2Rpn4fAp', 'images': [
                        {'height': 400, 'url': 'https://i.scdn.co/image/fd186774dc34bd456cd3dd77ffed99c7ff224108',
                         'width': 600},
                        {'height': 133, 'url': 'https://i.scdn.co/image/6e54f134e9491628dfbd4300e7d9791f81c0e0ec',
                         'width': 200},
                        {'height': 43, 'url': 'https://i.scdn.co/image/381555a8e2ac71b2770d5c36ff6b93be9a041955',
                         'width': 64}], 'name': 'Over It', 'popularity': 12, 'type': 'artist',
                     'uri': 'spotify:artist:7zn1qF9KcBCxwj2Rpn4fAp'},
                    {'external_urls': {'spotify': 'https://open.spotify.com/artist/1aEYCT7t18aM3VvM6y8oVR'},
                     'followers': {'href': None, 'total': 388459},
                     'genres': ['chicago punk', 'emo', 'pop punk', 'punk', 'skate punk'],
                     'href': 'https://api.spotify.com/v1/artists/1aEYCT7t18aM3VvM6y8oVR',
                     'id': '1aEYCT7t18aM3VvM6y8oVR', 'images': [
                        {'height': 640, 'url': 'https://i.scdn.co/image/ab6761610000e5ebb85da6fc072594f79f5f27f9',
                         'width': 640},
                        {'height': 320, 'url': 'https://i.scdn.co/image/ab67616100005174b85da6fc072594f79f5f27f9',
                         'width': 320},
                        {'height': 160, 'url': 'https://i.scdn.co/image/ab6761610000f178b85da6fc072594f79f5f27f9',
                         'width': 160}], 'name': 'Alkaline Trio', 'popularity': 54, 'type': 'artist',
                     'uri': 'spotify:artist:1aEYCT7t18aM3VvM6y8oVR'},
                    {'external_urls': {'spotify': 'https://open.spotify.com/artist/3zxKH0qp3nBCuPZCZT5Vaf'},
                     'followers': {'href': None, 'total': 1486447},
                     'genres': ['alternative metal', 'pop punk', 'post-grunge', 'socal pop punk'],
                     'href': 'https://api.spotify.com/v1/artists/3zxKH0qp3nBCuPZCZT5Vaf',
                     'id': '3zxKH0qp3nBCuPZCZT5Vaf', 'images': [
                        {'height': 640, 'url': 'https://i.scdn.co/image/ab6761610000e5ebf737c2d9bab95daf1e3c074c',
                         'width': 640},
                        {'height': 320, 'url': 'https://i.scdn.co/image/ab67616100005174f737c2d9bab95daf1e3c074c',
                         'width': 320},
                        {'height': 160, 'url': 'https://i.scdn.co/image/ab6761610000f178f737c2d9bab95daf1e3c074c',
                         'width': 160}], 'name': 'Yellowcard', 'popularity': 60, 'type': 'artist',
                     'uri': 'spotify:artist:3zxKH0qp3nBCuPZCZT5Vaf'}
                    ]

cache_file = "../cache/artist_tracks_cache"

pax_217 = {'external_urls': {'spotify': 'https://open.spotify.com/artist/52BrJWa29mZPy5hgDIs6d0'},
           'followers': {'href': None, 'total': 5311}, 'genres': ['christian punk'],
           'href': 'https://api.spotify.com/v1/artists/52BrJWa29mZPy5hgDIs6d0', 'id': '52BrJWa29mZPy5hgDIs6d0',
           'images': [
               {'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b27387dc08052e2e7ec0d5200249', 'width': 640},
               {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e0287dc08052e2e7ec0d5200249', 'width': 300},
               {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d0000485187dc08052e2e7ec0d5200249', 'width': 64}],
           'name': 'Pax217', 'popularity': 18, 'type': 'artist', 'uri': 'spotify:artist:52BrJWa29mZPy5hgDIs6d0'}
songs = Songs(sp)
selected_songs = songs.get_random_songs([pax_217], 5, cache_file, True, {}, favorite_artists)

idx = 0
for song in selected_songs:
    if song is not None:
        print(idx, song["artists"][0]["name"], song["name"])
        idx += 1

blink_182 = {'external_urls': {'spotify': 'https://open.spotify.com/artist/6FBDaR13swtiWwGhX1WQsP'},
             'followers': {'href': None, 'total': 8104564},
             'genres': ['alternative metal', 'modern rock', 'pop punk', 'punk', 'rock', 'socal pop punk'],
             'href': 'https://api.spotify.com/v1/artists/6FBDaR13swtiWwGhX1WQsP', 'id': '6FBDaR13swtiWwGhX1WQsP',
             'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab6761610000e5eb5da36f8b98dd965336a1507a',
                         'width': 640},
                        {'height': 320, 'url': 'https://i.scdn.co/image/ab676161000051745da36f8b98dd965336a1507a',
                         'width': 320},
                        {'height': 160, 'url': 'https://i.scdn.co/image/ab6761610000f1785da36f8b98dd965336a1507a',
                         'width': 160}], 'name': 'blink-182', 'popularity': 79, 'type': 'artist',
             'uri': 'spotify:artist:6FBDaR13swtiWwGhX1WQsP'}
selected_songs = songs.get_random_songs([blink_182, pax_217], 5, cache_file, True, {})

idx = 0
for song in selected_songs:
    if song is not None:
        print(idx, song["artists"][0]["name"], song["name"])
        idx += 1
