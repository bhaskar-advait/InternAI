import streamlit as st

st.set_page_config(page_title="InternAI Chat", page_icon="🤖")

st.title("🤖 InternAI - Mini ChatGPT (Offline AI)")

# chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# show chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# user input
user_input = st.chat_input("Ask anything about career, study, life...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    text = user_input.lower()

    # 🤖 smart response logic
    if "ai" in text or "technology" in text:
        reply = """AI is a great field 🚀  
👉 Learn Python + ML  
👉 Build projects  
👉 Try internships  
👉 Do Kaggle practice  

Do you want roadmap or free resources?"""

    elif "upsc" in text:
        reply = """UPSC needs consistency 📚  
👉 Start with NCERT  
👉 Daily current affairs  
👉 Answer writing practice  

Which subject do you like most?"""

    elif "iit" in text or "jee" in text:
        reply = """For IIT 🎯  
👉 Focus on Physics, Chemistry, Math  
👉 Solve PYQs  
👉 Daily practice  

Are you in class 11 or 12?"""

    elif "philosophy" in text:
        reply = """Interesting choice 🧠  
👉 Read Indian + Western philosophy  
👉 Can go for UPSC / teaching / writing  

Do you want career or knowledge guidance?"""

    elif "business" in text or "startup" in text:
        reply = """Entrepreneurship 🔥  
👉 Learn marketing & sales  
👉 Start small  
👉 Solve real problems  

What idea do you have in mind?"""

    elif "hello" in text or "hi" in text:
        reply = "Hello 👋 I'm your AI career guide. Tell me your goal or confusion."

    else:
        reply = """I can help with:  
👉 Career guidance  
👉 Skills roadmap  
👉 Study planning  

Tell me your interest (AI, UPSC, business, etc.)"""

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.write(reply)
