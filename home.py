import streamlit as st
import pandas as pd

st.title("😊😊Website Devloping using Python😊😊")
st.header("😊😊Website Devloping using Python😊😊")

st.image('./img/Thanadol.png')
st.subheader("Thanadol Phonin")

dt=pd.read_csv('./data/iris-3.csv')
st.header()
st.write(dt.head(10))