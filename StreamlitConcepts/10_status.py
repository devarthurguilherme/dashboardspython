import streamlit as st
import time

# Progress Bar
st.header("Progress Bar")
progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()

st.button("Return")


# Ballons
st.header("Ballons")
st.balloons()


# Spinner
st.header("Spinner")
with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')


# Snowflakes
st.header("Snowflakes")
st.snow()

# Error
st.header("Error")
st.error('This is an error', icon="🚨")


# Success
st.header("Success")
st.success('This is a success message!', icon="✅")
