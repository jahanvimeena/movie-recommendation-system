
import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_dict = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_dict:
         recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict=pickle.load(open('movies_dict.pkl', 'rb'))
movies =pd.DataFrame(movies_dict)

similarity= pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender System')
selected_movie_name= st.selectbox(
    'How would you like to contacted?',

movies['title'].values)

if st.button('Recommend'):
    recommendations= recommend(selected_movie_name)
    for j in recommendations:
      st.write(j)

