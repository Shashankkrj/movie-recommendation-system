import pickle
import bz2file as bz2
import requests
import streamlit as st
import pandas as pd


def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=642aacdc7deff1a72d9d750009e60278&language=en-US'.format(
            movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + str(data['poster_path'])


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:9]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


with open("movies.pkl", "rb") as f:
    movies = pd.read_pickle(f)

def decompress_pickle(file):
    data = bz2.BZ2File(file, "rb")
    data = pickle.load(data)
    return data


similarity = decompress_pickle('similarity.pbz2')

st.title('Movie Recommender System')
selected_movie_name = st.selectbox('Search', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col1:
        st.text(names[4])
        st.image(posters[4])
    with col2:
        st.text(names[5])
        st.image(posters[5])
    with col3:
        st.text(names[6])
        st.image(posters[6])
    with col4:
        st.text(names[7])
        st.image(posters[7])
