import streamlit as st
import requests


import pickle
st.set_page_config(
   page_title="Movie Recommendation",
   page_icon="🎬",
   layout="wide",
   initial_sidebar_state="expanded"
)

#fetching the posters to display
def fetch_poster(movie_id):
   response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=5d8d8534ad98ce3b55e750a43af8bd88'.format(movie_id))
   data =response.json()

   print(data)
   return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


#Recommendation Function
def recommend(name):
   index = movies[movies['title'] == name].index[0]
   distance = similarity[index]
   movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
   recommend_movie=[]
   recommend_movie_poster=[]
   for i in movies_list:

      movie_index=movies['id'][i[0]]
      recommend_movie.append(movies['title'][i[0]])
      recommend_movie_poster.append(fetch_poster(movie_index))
   return recommend_movie, recommend_movie_poster

movies = pickle.load(open('movies.pkl','rb'))
#movies=pd.read
similarity = pickle.load(open('similarity.pkl','rb'))




#Title
st.title("Movie Recommendations by Vasu")


#Drop Down Options
movies_list=pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_list['title'].values

#Search Bar
option = st.selectbox('Select the movie',movies_list)

#button
if st.button("Recommend Me"):
   output , posters = recommend(option)
   col1, col2, col3, col4, col5 = st.columns(5)
   with col1:
      st.subheader(output[0])
      st.image(posters[0])
   with col2:
      st.subheader(output[1])
      st.image(posters[1])
   with col3:
      st.subheader(output[2])
      st.image(posters[2])
   with col4:
      st.subheader(output[3])
      st.image(posters[3])
   with col5:
      st.subheader(output[4])
      st.image(posters[4])






