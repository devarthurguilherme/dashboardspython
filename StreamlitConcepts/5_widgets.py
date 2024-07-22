# https://docs.streamlit.io/develop/api-reference/widgets

import streamlit as st
import pandas as pd
import numpy as np

st.header("Button")
st.button("Reset", type="primary")

if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")


st.header("Download Button")


@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("utf-8")


my_large_df = pd.DataFrame(np.random.randn(20, 3), columns=["alex", "b", "c"])
csv = convert_df(my_large_df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name="large_df.csv",
    mime="text/csv",
)


st.header("Checkbox")
agree = st.checkbox("I agree")

if agree:
    st.write("Great!")
else:
    st.write("Read a terms!")


st.header("Radio")
genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")
