def get_response(text):
    text = text.lower()

    # 🎯 GATE
    if "gate" in text:
        return """🎯 GATE Preparation + Internship Path:

📚 Preparation:
- Focus on core subjects (branch specific)
- Solve PYQs
- Mock tests weekly

💼 Internships:
- Research Intern (IIT/NIT)
- Subject Expert Intern (Chegg, CourseHero)
- Teaching Assistant

🚀 Next Step:
Start preparing + apply for academic internships

👉 Which branch are you from?"""

    # 🎯 UPSC
    elif "upsc" in text:
        return """📚 UPSC + Career Path:

📖 Preparation:
- NCERT + Current Affairs
- Answer writing
- Mock tests

💼 Internships:
- NGO Intern
- Policy Research Intern
- Social Work Projects

🚀 Next Step:
Work with NGOs + build profile

👉 Optional subject decide kiya?"""

    # 🎯 AI / Data Science
    elif "ai" in text or "data science" in text:
        return """🤖 AI Career + Internship:

📚 Skills:
- Python, ML, Deep Learning
- Projects (very important)

💼 Internships:
- Data Science Intern
- ML Intern
- AI Research Intern

🌐 Platforms:
- Internshala
- LinkedIn
- Kaggle

🚀 Next Step:
Build 2–3 projects + apply daily

👉 Beginner ho ya already coding aati hai?"""

    # 🎯 Business / Startup
    elif "business" in text or "startup" in text:
        return """💼 Business + Internship:

📚 Skills:
- Marketing, Sales, Finance

💼 Internships:
- Marketing Intern
- Sales Intern
- Startup Intern

🚀 Next Step:
Join startup + learn practical skills

👉 Online business ya offline?"""

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

🚀
