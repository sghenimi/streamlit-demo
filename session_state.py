import streamlit as st

st.title("Session by example")

count = 0

if 'count' not in st.session_state:
    st.session_state['count'] = count


btn_increment = st.button("Increment")
if btn_increment:
    count += 2     

st.write(count)


for item in st.session_state.items:
    st.write(item)