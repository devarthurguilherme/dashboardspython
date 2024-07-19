

import streamlit as st

st.title("App Streamlit")
st.markdown("Streamlit is **Magnific**!")
st.header("This is a header!")
st.subheader("This is a subheader!")
st.caption("This is a captions, that means it is a text in small font!")
st.code("print('Hello Worl')")
st.text("Hello World!")
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
