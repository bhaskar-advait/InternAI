
import streamlit as st
import pandas as pd

data = pd.read_csv("data.csv")

st.title("InternAI")

skill = st.text_input("Enter Skill")
interest = st.text_input("Enter Interest")

if st.button("Recommend"):
    match = data[
        (data["skill"] == skill.lower()) &
        (data["interest"] == interest.lower())
    ]

    if not match.empty:
        st.success(match.iloc[0]["recommendation"])
    else:
        st.error("No match found")
