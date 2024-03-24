import streamlit as st

from autorag.cli.commands.configure.ui.util import (
    remove_streamlit_header_and_footer_menus,
    show_button_to_page,
    show_sidebar_menu,
)

remove_streamlit_header_and_footer_menus()
show_sidebar_menu()

st.title("AutoRAG 💫 Configuration")
st.text("Hello, this is Summary page!")


col1, _, col3 = st.columns([1, 1, 1])
with col1:
    show_button_to_page(page_nickname="finish", label="Finish", icon="🏁")
with col3:
    show_button_to_page(page_nickname="finish", label="Restart", icon="🔄")
