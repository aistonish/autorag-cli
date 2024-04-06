import streamlit as st

from autorag.cli.commands.configure.ui.util import remove_streamlit_header_and_footer_menus, show_button_to_page

remove_streamlit_header_and_footer_menus()

st.title("AutoRAG 💫 Configuration")
st.text("Hello, this is Intro page!")

show_button_to_page(page_nickname="weaviate", label="Next", icon="➡️")