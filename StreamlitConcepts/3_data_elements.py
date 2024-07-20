# https://docs.streamlit.io/develop/api-reference/data

import streamlit as st
import pandas as pd
import numpy as np

# Dataframes
st.header("Using Dataframe")
df = pd.DataFrame(np.random.randn(50, 20), columns=(
    "col %d" % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)


# Static Tables
st.header("Using Static Tables")
df1 = pd.DataFrame(np.random.randn(10, 5), columns=(
    "col %d" % i for i in range(5)))
st.table(df1)


# Metrics
st.header("Using Metrics")
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")


# JSON
st.header("Using Dicts and JSON")
st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})
