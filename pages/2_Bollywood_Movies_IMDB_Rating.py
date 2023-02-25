import streamlit as st 
from matplotlib import image
import pandas as pd
import plotly.express as px
import os 

FILE_DIR = os.path.dirname(os.path.abspath(__file__))

PARENT_DIR = os.path.join(FILE_DIR, os.pardir)

dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "bollywood.jpg")
DATA_PATH = os.path.join(dir_of_interest, "Data", "movies_data.csv")

st.title("Dashboard - :green[Bollywood Movies IMDB Ratings]")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

Genre = st.selectbox("Select the Genre:", df['Genre'].unique())
# Type = st.selectbox("Select the Type:", df['Type'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['Genre'] == Genre], y="Rating")
col1.plotly_chart(fig_1, use_container_width=True)

