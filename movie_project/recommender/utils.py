import requests

API_KEY = "99aec3747429a8a2d2620182141a503d"

def fetch_poster(movie_title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_title}"
    
    data = requests.get(url).json()

    if data['results']:
        poster_path = data['results'][0]['poster_path']
        return f"https://image.tmdb.org/t/p/w500{poster_path}"

    return "https://via.placeholder.com/300x450"