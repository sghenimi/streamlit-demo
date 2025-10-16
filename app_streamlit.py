import streamlit as st

@st.fragment
def fragment_function():
    if st.button("Hi!"):
        st.write("Hi back!")

with st.sidebar:
    fragment_function()
