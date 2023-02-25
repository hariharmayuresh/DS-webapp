import streamlit as st

name = ":blue[Mayuresh] :blue[Harihar]"
bio = ":green[Data Science enthusiast] and Intern at Innomatics :red[Research Labs]"
linkedin_url = "https://www.linkedin.com/in/mayuresh-harihar-2a170721a/"
github_url = "https://github.com/hariharmayuresh"
instagram_url = "https://www.instagram.com/hariharmayuresh/"

photo_url = "resources/images/profile_photo.png" 
st.image(photo_url, width=300)

st.title(name)
st.header(bio)

st.subheader("Connect with me on:")
st.subheader(f"[LinkedIn]({linkedin_url})")
st.subheader(f"[GitHub]({github_url})")
st.subheader(f"[Instagram]({instagram_url})")
