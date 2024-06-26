import streamlit as st
import pickle

movies=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    for i in movies_list:
        movie_id=i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

st.title('Movie Recommendation System')



selected_movie=st.selectbox(
    'Which movies you have watched recently?',
    (movies['title'].values)
)

if(st.button('Recommend')):
    st.write('Great!, Now you should watch the following movies:')
    for i in recommend(selected_movie):
        st.write(i)