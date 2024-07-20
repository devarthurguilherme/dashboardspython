# https://docs.streamlit.io/develop/api-reference/charts
# https://matplotlib.org/stable/plot_types/basic/bar.html#sphx-glr-plot-types-basic-bar-py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Line Chart
st.header("Line Chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["alex", "b", "c"])

st.line_chart(chart_data)


# Simple Area Chart
st.header("Simple Area Chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)


# Simple Bar Charts
st.header("Simple Bar Charts")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)


# Scatterplot
st.header("Scatterplot")

df2 = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [41.464630, -8.543770],
    columns=['lat', 'lon'])

st.map(df2)


# Matplotlib Graphics
st.header("Matplotlib")

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
