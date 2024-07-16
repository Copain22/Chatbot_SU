import streamlit as st


def init_chat_history():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

def add_message(user_message, bot_response):
    st.session_state.chat_history.append({"user": user_message, "bot": bot_response})

init_chat_history()

st.title("Simple Chatbot")

# Input Message
user_message = st.text_input("Enter your message:")

if user_message:
    bot_response = f"Thank you for telling me {user_message}"
    add_message(user_message, bot_response)

# Display Chat
for chat in st.session_state.chat_history:
    st.write(f"**User:** {chat['user']}")
    st.write(f"**Bot:** {chat['bot']}")