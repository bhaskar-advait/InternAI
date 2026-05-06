import streamlit as st
import requests

st.title("🤖 InternAI - Smart Career AI")

user_input = st.text_input("Enter your interest, goal, or skill")

if st.button("Recommend"):

    if user_input.strip() == "":
        st.warning("⚠️ Please enter something")
    else:
        url = "https://chatgpt-42.p.rapidapi.com/conversationgpt4"

        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": f"Suggest career path for: {user_input}"
                }
            ],
            "system_prompt": "You are a career expert. Give clear guidance with steps.",
            "temperature": 0.7,
            "top_k": 5,
            "top_p": 0.9,
            "max_tokens": 300
        }

        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "abc8f24941msh2b05739e813230ep1c2db0jsnb5cc6114bbe6",
            "X-RapidAPI-Host": "chatgpt-42.p.rapidapi.com"
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            result = response.json()

            st.success(result['result'])

        except:
            st.error("❌ API error, try again later")
