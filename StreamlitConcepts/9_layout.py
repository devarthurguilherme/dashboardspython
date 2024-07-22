import streamlit as st
import numpy as np
import time

st.header("Sidebar")
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )


st.header("Columns")
col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("StreamlitConcepts\meusArquivos\img2.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")


# Expander
st.header("Expander")
st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')
    st.image("https://static.streamlit.io/examples/dice.jpg")


# Container
st.header("Container")
with st.container():
    st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(5, 3))

st.write("This is outside the container")


# Empty
st.header("Empty")
placeholder = st.empty()
with st.empty():
    for seconds in range(10):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
#     st.write("✔️ 10 seconds over!")
        # Replace the placeholder with some text:
        placeholder.text("Hello")
        # Replace the text with a chart:
        placeholder.line_chart({"data": [1, 5, 2, 6]})


# Replace the chart with several elements:
with placeholder.container():
    st.write("This is one element")
    st.write("This is another")

# Clear all those elements:
# placeholder.empty()
