import streamlit as st
from pipeline.pipeline import AnimeRecommenderPipeline

from dotenv import load_dotenv
load_dotenv()

st.set_page_config(
  page_title="Anime Recommender",
  layout="wide"
)

@st.cache_resource
def init_pipeline():
  return AnimeRecommenderPipeline()

pipeline = init_pipeline()

st.title("Anime Recommender System")
query = st.text_input("Enter your anime preferences? eg. light hearted anime in school setting")
if query:
  with st.spinner("Fetching recommendations for you ..."):
    response = pipeline.recommend(query)
    st.markdown("### Recommendations")
    st.write(response)

