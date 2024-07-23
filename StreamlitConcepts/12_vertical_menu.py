import streamlit as st
from streamlit_option_menu import option_menu

# Sidebar
# with st.sidebar:
#     selecao = option_menu(
#         menu_title="App",
#         options=["Inicio", "Projetos", "Contato"]
#     )

# Horizontal Menu
selecao = option_menu(
    menu_title="App",
    options=["Inicio", "Projetos", "Contato"],
    icons=["house", "book", "envelope"],
    menu_icon="cast",
    orientation="horizontal"
)
if selecao == "Inicio":
    st.title(f"Você selecionou o menu {selecao}")
if selecao == "Projetos":
    st.title(f"Você selecionou o menu {selecao}")
if selecao == "Contato":
    st.title(f"Você selecionou o menu {selecao}")
