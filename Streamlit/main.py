import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

tag = st.selectbox('Choose a topic', [
    'Love', 'Inspirational', 'Life', 'Humor', 'Books', 'Reading', 'Friendship',
    'Friends', 'Truth'
])
url = f"https://quotes.toscrape.com/tag/{tag}/"
res = requests.get(url)

content = BeautifulSoup(res.content, 'html.parser')
quotes = content.find_all('div', class_='quote')
for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    link = quote.find('a')
    st.success(text)
    st.markdown(f"<a href=https://quotes.toscrape.com{link['href']}>{author} </a>", unsafe_allow_html=True)