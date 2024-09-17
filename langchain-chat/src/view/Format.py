import time

import streamlit as st


def display_format_source(sources: list):
    st.markdown("**Sources:**")
    source_container = """
    <style>
        .source-block {{
            padding: 4px;
            border: 1px solid #ccc;
            border-radius: 3px;
            max-width: 300px;
            word-wrap: break-word;
            overflow: hidden;
            transition: transform 0.3s ease, background-color 0.3s ease, box-shadow 0.3s ease;
            margin: 8px;
        }}

        /* Hover effect: Scale, background color, and shadow */
        .source-block:hover {{
            transform: scale(1.08);
            background-color: #fffacd; /* Light background color */
            color: #333333; /* Dark gray text color */
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }}

        .source-container {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            padding: 10px;
            border-radius: 5px;
        }}
    </style>

    <div class='source-container'>
        {}
    </div>
    """

    limited_sources = sources[:3]
    limited_sources = [source.split("/")[-1] for source in limited_sources]
    file_icon = "📄"
    source_blocks = "".join([f"<div class='source-block'>{file_icon} {source}</div>" for source in limited_sources])

    st.markdown(source_container.format(source_blocks), unsafe_allow_html=True)


def dynamic_spinner():
    spinner_placeholder = st.empty()
    messages = [
        "Generating response...",
        "Still working on it...",
        "Almost there...",
        "Just a few seconds more...",
    ]

    for _, message in enumerate(messages):
        with spinner_placeholder:
            with st.spinner(message):
                time.sleep(5)

    spinner_placeholder.empty()
