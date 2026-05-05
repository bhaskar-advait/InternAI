import streamlit as st

st.title("🌍 Universal Career AI Guide")

user_input = st.text_input("Enter your interest, goal, or skill")

if st.button("Recommend"):

    text = user_input.lower()

    # 🔹 Dictionary of fields
    career_map = {
        "ai data science": ["python", "ai", "ml", "data", "analytics"],
        "web development": ["web", "html", "css", "frontend", "design"],
        "software development": ["java", "c++", "coding", "programming"],
        "cyber security": ["hacking", "security", "cyber"],
        "civil services (upsc)": ["upsc", "ias", "government"],
        "engineering (iit/jee)": ["iit", "jee", "engineering"],
        "medical (doctor)": ["neet", "doctor", "medical"],
        "business / startup": ["business", "startup", "entrepreneur"],
        "law": ["law", "advocate", "legal"],
        "philosophy / spirituality": ["philosophy", "vedanta", "spiritual"],
        "teaching / education": ["teacher", "teaching", "education"],
        "finance": ["finance", "stock", "trading"],
        "arts / design": ["art", "drawing", "creative"],
        "media / content": ["youtube", "content", "media"],
        "sports": ["sports", "cricket", "football"],
    }

    found = False

    for career, keywords in career_map.items():
        for word in keywords:
            if word in text:
                st.success(f"🎯 Recommended Path: {career.title()}")
                found = True
                break
        if found:
            break

    # 🔥 Smart fallback (no "no match" ever)
    if not found:
        st.success("🎯 Recommended Path: Explore interdisciplinary careers")
        st.info("""
💡 You may explore:
- Technology + Business
- Philosophy + Psychology
- Content Creation + Education
- Social Work + Policy

👉 Start with your curiosity and build skills gradually.
""")
