import json
import logging
import os

import streamlit as st
from src.control.Markdown import read_markdown
from src.control.VertexAIChat import VertexAIChat

vertex = VertexAIChat()
MODEL_PATH = os.path.join(os.getcwd(), "src/model")


CHAT_HISTORY_FILE = "chat_history.json"


def load_chat_history():
    if os.path.exists(CHAT_HISTORY_FILE):
        with open(CHAT_HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


def save_chat_history(messages):
    with open(CHAT_HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(messages, file, ensure_ascii=False, indent=4)


def initizalize_chat_history():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "messages" not in st.session_state:
        st.session_state.messages = []


def show_chat_history():
    for message in st.session_state.chat_history:
        st.chat_message(message["role"]).write(message["content"])


# Initialize session state for messages if not already set
def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state["messages"] = load_chat_history()
        if not st.session_state["messages"]:
            st.session_state["messages"] = [
                {
                    "role": "assistant",
                    "content": read_markdown(os.path.join(MODEL_PATH, "greeting_content.md")),
                }
            ]

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [(msg["role"], msg["content"]) for msg in st.session_state["messages"]]


def get_response(prompt):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    messages = []

    llm_chain = vertex.initialize_llm_chain()
    response_search_immigration = None
    try:
        with st.spinner("Searching details from database..."):
            response_search_immigration = llm_chain.run(input=prompt, chat_history=st.session_state.chat_history)
    except Exception as e:
        logging.error(f"Failed to get response from search: {e}")
        response = "Sorry, there was an error processing your request. Please try again."

    # Prepare messages from chat history to pass to the LLM response generation
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            messages.append(vertex.get_HumanMessageContent(message))
        elif message["role"] == "assistant":
            messages.append(vertex.get_AIMessageContent(message))

    # Add RAG-based result to messages before generating LLM response
    with st.spinner("Generating response..."):
        if response_search_immigration:
            response = vertex.get_RAG_response(messages, response_search_immigration)
        else:
            response = vertex.get_response(messages)

    # Append assistant's response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": response.content})
    st.chat_message("assistant").write(response.content)
