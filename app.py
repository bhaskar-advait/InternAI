import streamlit as st

st.set_page_config(page_title="InternAI Chat", page_icon="🤖")

st.title("🤖 InternAI - Smart Career Chat")

# chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# show chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# response function
def get_response(text):
    text = text.lower()

    # 🎯 GATE
    if "gate" in text:
        return """🎯 GATE Preparation + Internship Path:

📚 Preparation:
- Focus on core subjects (branch specific)
- Solve PYQs
- Weekly mock tests

💼 Internships:
- Research Intern (IIT/NIT)
- Subject Expert (Chegg)
- Teaching Assistant

🚀 Next Step:
Start preparation + apply for academic internships

👉 Which branch are you from?
"""

    # 🎯 UPSC
    elif "upsc" in text:
        return """📚 UPSC Strategy + Internship:

📖 Preparation:
- NCERT (6–12)
- Current Affairs (The Hindu)
- Answer writing practice

💼 Internships:
- NGO Intern
- Policy Research Intern

🚀 Next Step:
Work with NGOs + build profile

👉 Optional subject decide kiya?
"""

    # 🎯 AI / Data Science
    elif "ai" in text or "data science" in text:
        return """🤖 AI Career + Internship:

📚 Skills:
- Python, Machine Learning
- Deep Learning basics
- Projects (very important)

💼 Internships:
- Data Science Intern
- ML Intern
- AI Intern

🌐 Platforms:
- Internshala
- LinkedIn
- Kaggle

🚀 Next Step:
Build 2–3 projects + apply daily

👉 Beginner ho ya already coding aati hai?
"""

    # 🎯 Business / Startup
    elif "business" in text or "startup" in text:
        return """💼 Business + Internship:

📚 Skills:
- Marketing
- Sales
- Finance basics

💼 Internships:
- Marketing Intern
- Sales Intern
- Startup Intern

🚀 Next Step:
Join startup + learn practical skills

👉 Online business ya offline?
"""

    # 🎯 Philosophy
    elif "philosophy" in text:
        return """🧠 Philosophy + Career:

📚 Skills:
- Critical thinking
- Writing

💼 Internships:
- Content Writer
- Research Intern
- Teaching Assistant

🚀 Next Step:
Start writing blogs + research

👉 Academic ya content side me interest hai?
"""

    # 🎯 IIT / JEE
    elif "iit" in text or "jee" in text:
        return """🎯 IIT-JEE + Future Internships:

📚 Preparation:
- Strong PCM
- PYQs + daily practice

💼 Future Internships:
- Tech Intern (after college)
- Research Intern (IIT labs)

🚀 Next Step:
Focus on JEE first

👉 Class 11 ya 12?
"""

    # 👋 Greeting
    elif "hi" in text or "hello" in text:
        return "Hello 👋 I'm your AI career guide. Tell me your goal."

    # 🔥 Default
    else:
        return f"""🤔 I understood: "{text}"

👉 Be more specific:
- AI career
- UPSC preparation
- GATE CSE
- Business idea

I'll guide you properly 👍
"""

# chat input
user_input = st.chat_input("Ask about career, exams, internships...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    reply = get_response(user_input)

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.write(reply)
