import streamlit as st
st.write('Select your gender. 1 - male, 2 - female')
st.selectbox('Gender',[1, 2])
st.selectbox('Do you smoke', [0, 1])
st.selectbox('Your cholesterol level', [1, 2, 3])
st.selectbox('Your gluc level', [1, 2, 3])
st.selectbox('Alco', [0, 1])
st.selectbox('Training', [0, 1])
