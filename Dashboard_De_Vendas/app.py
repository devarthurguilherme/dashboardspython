import streamlit as st
import plotly.express as px
from dataset import df
from helperFunctions import formatNumber

# Layout Wide Origin Config
st.set_page_config(layout='wide')

st.title("Dashboard de Vendas :shopping_trolley:")

# Tabs
datasetTab1, receitaTab2, vendedoresTab3 = st.tabs(
    ['Dataset', 'Receita', 'Vendedores'])

# Tab Dataset
with datasetTab1:
    # Show Full Dataframe
    st.dataframe(df)

# Tab Receita
with receitaTab2:
    # Show Columns
    column1, column2 = st.columns(2)
    # Metric 1: Total Price sum
    with column1:
        st.metric('Receita Total', formatNumber(df['Preço'].sum()))
    with column2:
        st.metric('Quantidade de Vendas', formatNumber(df.shape[0]))
