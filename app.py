import streamlit as st
import pickle
import pandas as pd
import requests

#Function to bring poster for the most similar 5 movies
def Bring_Poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d7c8a9817274467716856976542ab068&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

#Function would return recommended movie name and their posters
def recommend(movie):
    films_ind = movies[movies['title'] == movie].index[0]
    distances = similarity[films_ind]
    films_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie = []
    recommended_movie_poster = []
    for i in films_list:
        movies_id = movies.iloc[i[0]].id
        recommended_movie.append(movies.iloc[i[0]].title)
        # Bring Posters from API
        recommended_movie_poster.append(Bring_Poster(movies_id))
    return recommended_movie, recommended_movie_poster

#TITLE OF THE WEB : MOVIE RECOMMENDER SYSTEM
st.title('Movie Recommender System')

#Here movies will be loaded as dictionary
movies_dict = pickle.load(open('films_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

#this would create the select box in which we have to select a movie for which we need recommendations
selected_movie_name = st.selectbox(
     'Select a movie to get its recommendations!',
     (movies['title'].values))

#This would print the name and the posters of the similar movies to the one we have selected.
if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

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
    with col5:
        st.text(names[4])
        st.image(posters[4])


