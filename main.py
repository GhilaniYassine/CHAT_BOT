
import os
import json
import streamlit as st
import openai

# Load configuration
pwd = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{pwd}/config.json"))

# Set OpenAI API key
OPENAI_API_KEY = config_data['OPENAI_API_KEY']
openai.api_key = OPENAI_API_KEY

# Streamlit app settings
st.set_page_config(
    page_title="BASKET_WITH_KOBE",
    page_icon="🏀",
    layout="centered"
)

# Initialize chat sessions
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Streamlit page title
st.title("QA_WITH_KOBE")

# Display the chat history
for message in st.session_state.chat_history:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# User input prompt
user_prompt = st.chat_input('Ask KOBE?')

if user_prompt:
    # Add user message to chat history and display it
    st.chat_message('user').markdown(user_prompt)
    st.session_state.chat_history.append({'role': 'user', 'content': user_prompt})

    # Send the user prompt to OpenAI
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[
            {'role': 'system', 'content': 'You are an expert in basketball like Kobe.'},
            *st.session_state.chat_history
        ]
    )

    # Extract the assistant's response
    assistant_response = response.choices[0].message['content']
    st.session_state.chat_history.append({'role': 'assistant', 'content': assistant_response})
    with st.chat_message('assistant'):
        st.markdown(assistant_response)
