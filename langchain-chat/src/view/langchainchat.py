import os

import streamlit as st
from src.control.config import PORT_NUMBER, caption, title
from src.control.HandleStreamlit import (
    get_response,
    initizalize_chat_history,
    show_chat_history,
)

port = int(os.environ.get("PORT", PORT_NUMBER))


# Main application function
def application():
    st.set_page_config(page_title=title)
    st.title(title)
    st.caption(caption)

    # Initialize session state for messages
    initizalize_chat_history()
    show_chat_history()

    if prompt := st.chat_input("Ask me anything!"):
        get_response(prompt)
