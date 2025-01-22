import streamlit as st
import pickle
import pandas as pd 

def recomend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similarity[movie_index]
    movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    
    recomended_movies=[]
    for i in movie_list:
        recomended_movies.append(movies.iloc[i[0]].title)
    return recomended_movies

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))


st.title('Recomendation System')


selected_movie =st.selectbox(
    "What kind of movies you like to watch?",
    movies['title'].values
)

if st.button('Recomend'):
    recomendation=recomend(selected_movie)
    for i in recomendation:
        st.write(i)