import streamlit as st
import os
from openai import OpenAI

# 🔐 API key from secrets
client = OpenAI(api_key=os.getenv("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"))

st.set_page_config(page_title="InternAI Chat", page_icon="🤖")

st.title("🤖 InternAI - AI Career Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! 👋 Tell me your interests, goals, or confusion. I'll guide your career."}
    ]

# Display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Type your interest, goal, or question...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤖"):

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a career guidance expert. Ask follow-up questions if needed and give clear, practical advice."}
                ] + st.session_state.messages
            )

            reply = response.choices[0].message.content

            st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
