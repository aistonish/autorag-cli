import streamlit as st

from autorag.cli.commands.configure.ui.util import (
    exit_app,
    remove_streamlit_header_and_footer_menus,
)

remove_streamlit_header_and_footer_menus()

st.title("Thanks! ❤️")
st.markdown("""
# AutoRAG 💫 is now ready to launch 🚀
❌ *You can close this tab or window...* ❌
""")

exit_app()
