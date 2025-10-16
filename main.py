import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

def page_2():
    st.title("Page 2")


pg = st.navigation(["uber_pickups.py", page_2])
pg.run()
