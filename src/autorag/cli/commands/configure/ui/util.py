import os
import time

import psutil
import streamlit as st

PAGES = {
    "Introduction": "pages/intro.py",
    "Configure Weaviate": "pages/config_weaviate.py",
    "Configure LLM": "pages/config_llm.py",
    "Summary": "pages/summary.py",
    "Finish": "pages/finish.py",
}


def setup_state():
    if "page" not in st.session_state:
        st.session_state.page = 0


def exit_app():
    time.sleep(1)
    pid = os.getpid()
    p = psutil.Process(pid)
    p.terminate()


def show_sidebar_menu():
    for label, page in PAGES.items():
        st.sidebar.page_link(page, label=label)


def show_button_to_page(
    page_nickname: str | None = None,
    page: str | None = None,
    label: str | None = None,
    icon: str | None = None,
):
    if page_nickname:
        for label_, page_ in PAGES.items():
            if page_nickname in page_.lower():
                st.page_link(label=label_ if label is None else label, page=page_, icon=icon)
    elif page and label:
        st.page_link(label=label, page=page, icon=icon)
    else:
        st.write("No page found")


def remove_streamlit_header_and_footer_menus():
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
