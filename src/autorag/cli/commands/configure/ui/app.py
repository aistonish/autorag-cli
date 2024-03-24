import streamlit as st

from autorag.cli.commands.configure.ui.util import setup_state, show_button_to_page

st.set_page_config(
    page_title="AutoRAG 💫 Configuration",
    page_icon="⚙️",
)

setup_state()

# remove the Streamlit header menu and footer
# https://discuss.streamlit.io/t/hide-deploy-and-streamlit-mainmenu/52433/2
st.markdown(
    """
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""",
    unsafe_allow_html=True,
)


st.markdown("# Welcome to the AutoRAG 💫 Configurator ⚙️")

show_button_to_page(page_nickname="intro", label="Start Configuration", icon="➡️")
