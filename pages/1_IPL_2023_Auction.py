import streamlit as st 
from matplotlib import image
import pandas as pd
import plotly.express as px
import os 

FILE_DIR = os.path.dirname(os.path.abspath(__file__))

PARENT_DIR = os.path.join(FILE_DIR, os.pardir)

dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "ipl_auction.jpeg")
DATA_PATH = os.path.join(dir_of_interest, "Data", "ipl_2023_dataset.csv")

st.title("Dashboard - :blue[IPL 2023 Auction]")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

Team = st.selectbox("Select the Team:", df['Team'].unique()) 

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['Team'] == Team], x="Type")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.histogram(df[df['Team'] == Team], y="Price Cr")
col2.plotly_chart(fig_2, use_container_width=True)

