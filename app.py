import streamlit as st

st.set_page_config(page_title="InternAI Chat", page_icon="🤖")

st.title("🤖 InternAI - Smart Career Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask about career, exams, roadmap...")

def get_response(text):
    text = text.lower()

    # 🎯 GATE
    if "gate" in text:
        return """🎯 GATE Preparation Guide:
👉 Subjects: Core subjects (branch specific)
👉 Strategy:
- Complete syllabus once
- Solve PYQs (most important)
- Mock tests weekly
👉 Resources:
- Made Easy / ACE Academy notes
👉 Timeline:
- 6–12 months serious prep

Which branch are you from?"""

    # 🎯 UPSC
    elif "upsc" in text:
        return """📚 UPSC Strategy:
👉 Start with NCERT (6–12)
👉 Daily newspaper (The Hindu)
👉 Subjects: Polity, History, Geography, Economy
👉 Practice answer writing
👉 Give mock tests

Do you need subject-wise plan?"""

    # 🎯 IIT / JEE
    elif "iit" in text or "jee" in text:
        return """🎯 IIT-JEE Preparation:
👉 Focus on PCM
👉 Solve PYQs + coaching modules
👉 Daily practice (6–8 hrs)
👉 Strong concepts + revision

Are you in class 11 or 12?"""

    # 🎯 AI / Tech
    elif "ai" in text or "data science" in text:
        return """🤖 AI Roadmap:
👉 Learn Python
👉 Math basics (stats, linear algebra)
👉 Machine Learning
👉 Projects (very important)
👉 Internship / Kaggle

Beginner ho ya thoda experience hai?"""

    # 🎯 Business
    elif "business" in text or "startup" in text:
        return """💼 Business Guide:
👉 Learn marketing + sales
👉 Solve real-world problem
👉 Start small
👉 Build network

Tumhara idea kya hai?"""

    # 🎯 Philosophy
    elif "philosophy" in text:
        return """🧠 Philosophy Path:
👉 Read: Vedanta, Buddha, Western philosophy
👉 Career:
- Teaching
- Writing
- UPSC optional
👉 Practice thinking + writing

Career chahiye ya knowledge depth?"""

    # 🎯 Default (smart fallback)
    else:
        return f"""🤔 I understood you said: "{text}"

👉 Try being more specific:
- Career (AI, UPSC, GATE, business)
- Goal (job, exam, skill)

Example: "GATE preparation for CSE"  
I'll guide you properly 👍"""

# chat flow
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    reply = get_response(user_input)

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.write(reply)
