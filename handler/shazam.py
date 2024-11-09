import requests


def search_shazam(term, limit):
    url = "https://www.shazam.com/services/amapi/v1/catalog/UZ/search"
    params = {
        "term": term,
        "limit": limit,
        "offset": 0,
        "types": "songs"
    }
    response = requests.get(url, params=params)
    data = response.json()
    songs_info = []
    try:
        songs = data['results']['songs']['data']
        for song in songs:
            song_info = {
                'title': song['attributes']['name'],
                'artist': song['attributes']['artistName'],
                'preview_url': song['attributes']['previews'][0]['url']
            }
            songs_info.append(song_info)
        return songs_info
    except (KeyError, IndexError):
        return None