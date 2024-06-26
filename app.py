import streamlit as st
import pickle
import requests


def fetch_movie_image(id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b83372fae972a9fcdb7da6903903fe6c&language=en.US'.format(id))
    response=response.json()
    print(response)
    return "https://image.tmdb.org/t/p/w500/"+response['poster_path']


movies=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_image=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_image.append(fetch_movie_image(movies.iloc[i[0]].id))
    return recommended_movies,recommended_movies_image

st.title('Movie Recommendation System')



selected_movie=st.selectbox(
    'Which movies you have watched recently?',
    (movies['title'].values)
)

if(st.button('Recommend')):
    st.write('Great!, Now you should watch the following movies:')
    movie_name,movie_image=recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
       st.text(movie_name[0])
       st.image(movie_image[0])
    with col2:
       st.text(movie_name[1])
       st.image(movie_image[1])
    with col3:
       st.text(movie_name[2])
       st.image(movie_image[2])
    with col4:
       st.text(movie_name[3])
       st.image(movie_image[3])
    with col5:
       st.text(movie_name[4])
       st.image(movie_image[4])
    