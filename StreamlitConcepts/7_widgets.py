# https://docs.streamlit.io/develop/api-reference/widgets
import datetime
import streamlit as st
import pandas as pd
from io import StringIO


st.header("Date Input")
d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write("Your birthday is:", d)

st.header("Time Input")
t = st.time_input("Set an alarm for", datetime.time(8, 45))
st.write("Alarm is set for", t)


st.header("File Uploader")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)


st.header("Camera Input")
picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)


st.header("Color Picker")
color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)
