import streamlit as st
from google import genai
import os

os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]

st.title("My AI Chat")

@st.cache_resource
def get_client():
    return genai.Client()

client = get_client()

if "chat" not in st.session_state:
    st.session_state.chat = client.chats.create(model="gemini-3.6-flash")
    st.session_state.messages = []

for role, text in st.session_state.messages:
    with st.chat_message(role):
        st.write(text)

user_input = st.chat_input("Say something...")

if user_input:
    st.session_state.messages.append(("user", user_input))
    with st.chat_message("user"):
        st.write(user_input)

    response = st.session_state.chat.send_message(user_input)

    st.session_state.messages.append(("assistant", response.text))
    with st.chat_message("assistant"):
        st.write(response.text)
