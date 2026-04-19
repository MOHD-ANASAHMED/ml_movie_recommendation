# # recommend.py

# import pickle

# movies = pickle.load(open('movies.pkl', 'rb'))
# similarity = pickle.load(open('similarity.pkl', 'rb'))

# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = similarity[index]
    
#     movies_list = sorted(
#         list(enumerate(distances)),
#         reverse=True,
#         key=lambda x: x[1]
#     )[1:6]

#     recommended_movies = []

#     for i in movies_list:
#         recommended_movies.append(movies.iloc[i[0]].title)

#     return recommended_movies

import os
import pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

movies_path = os.path.join(BASE_DIR, 'movies.pkl')
similarity_path = os.path.join(BASE_DIR, 'similarity.pkl')

movies = pickle.load(open(movies_path, 'rb'))
similarity = pickle.load(open(similarity_path, 'rb'))


def recommend(movie):
    if movie not in movies['title'].values:
        return []

    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    return [movies.iloc[i[0]].title for i in movies_list]