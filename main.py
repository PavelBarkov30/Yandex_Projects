import streamlit as st
st.write('Select your gender. 1 - male, 2 - female')
st.checkbox('Gender',[1, 2])
st.checkbox('Do you smoke', [0, 1])
st.checkbox('Your cholesterol level', [1, 2, 3])
st.checkbox('Your gluc level', [1, 2, 3])
st.checkbox('Alco', [0, 1])
st.checkbox('Training', [0, 1])