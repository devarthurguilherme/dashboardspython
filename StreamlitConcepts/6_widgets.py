# https://docs.streamlit.io/develop/api-reference/widgets
import streamlit as st


st.header("Select Box")
option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"))

st.write("You selected:", option)


st.header("Multiselect")
options = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"])

st.write("You selected:", options)


st.header("Select Slider")
color = st.select_slider(
    "Select a color of the rainbow",
    options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"])
st.write("My favorite color is", color)


st.header("Input")
title = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", title)

st.header("Number Input")
number = st.number_input("Insert a number")
st.write("The current number is ", number)


st.header("Textarea")
txt = st.text_area(
    "Text to analyze",
    "It was the best of times, it was the worst of times, it was the age of "
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...)",
)

st.write(txt)
st.write(f"You wrote {len(txt)} characters.")
