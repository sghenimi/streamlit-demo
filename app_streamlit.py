import streamlit as st
import pandas as pd
import numpy as np

"st.session_state object : ", st.session_state

ti_name = st.text_input("Your name", key="name")
sl_value = st.slider('Entrered value')  # this is a widget

st.write(ti_name, sl_value, 'squared is', sl_value * sl_value)



df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

"You selected: ", option


if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

import streamlit as st

# Add a selectbox to the sidebar:
sb_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
sb_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
"You selected: ", sb_slider

for item in st.session_state.items():
    st.write(item)


import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

