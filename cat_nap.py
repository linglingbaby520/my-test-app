import streamlit as st
import requests

st.title("🐾 Cat Nap")
st.write("Click to see a random cat!")

def get_cat():
    r = requests.get("https://api.thecatapi.com/v1/images/search")
    return r.json()[0]["url"]

if "url" not in st.session_state:
    st.session_state.url = get_cat()

if st.button("New Cat 🐱"):
    st.session_state.url = get_cat()

st.image(st.session_state.url)
