# from django.shortcuts import render
# from .recommend import recommend
# import pickle
# import os

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # movies = pickle.load(open(os.path.join(BASE_DIR, '..', 'movies.pkl'), 'rb'))
# movies = pickle.load(open(os.path.join(BASE_DIR, 'movies.pkl'), 'rb'))

# def home(request):
#     movie_list = movies['title'].values

#     if request.method == "POST":
#         selected_movie = request.POST.get('movie')
#         recommendations = recommend(selected_movie)

#         return render(request, 'index.html', {
#             'movies': movie_list,
#             'recommendations': recommendations
#         })

#     return render(request, 'index.html', {'movies': movie_list})

from django.shortcuts import render
from .recommend import recommend
from .utils import fetch_poster
import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
movies = pickle.load(open(os.path.join(BASE_DIR, 'movies.pkl'), 'rb'))

def home(request):
    movie_list = movies['title'].values

    if request.method == "POST":
        selected_movie = request.POST.get('movie')

        names = recommend(selected_movie)

        posters = [fetch_poster(name) for name in names]

        results = zip(names, posters)

        return render(request, 'index.html', {
            'movies': movie_list,
            'results': results
        })

    return render(request, 'index.html', {'movies': movie_list})