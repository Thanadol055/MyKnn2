import streamlit as st
import pandas as pd

st.title("😊😊Website Devloping using Python😊😊")
st.header("😊😊Website Devloping using Python😊😊")

st.image('./img/Photo.jpg')
st.subheader("Thanadol Phonin")

dt=pd.read_csv('./data/iris.csv')
st.header("ข้อมูลดอกไม้")
st.write(dt.head(10))