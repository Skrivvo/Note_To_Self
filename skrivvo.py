import streamlit as st
import datetime

# Function to get mood-based theme
def get_theme(mood):
    themes = {
        "Happy": "#FFD700",  # Gold
        "Sad": "#4682B4",  # Steel Blue
        "Neutral": "#808080",  # Gray
        "Excited": "#FF4500",  # Orange Red
        "Relaxed": "#98FB98"  # Pale Green
    }
    return themes.get(mood, "#FFFFFF")

# Ask for user's mood
st.title("Digital Journal")
st.subheader("How are you feeling today?")
user_mood = st.selectbox("Select your mood:", ["Happy", "Sad", "Neutral", "Excited", "Relaxed"])

# Apply theme based on mood
theme_color = get_theme(user_mood)
st.markdown(f"""
    <style>
        .main {{
            background-color: {theme_color};
        }}
    </style>
""", unsafe_allow_html=True)

# Journal Sections
st.header("📖 My Digital Journal")

# Mood Tracker
st.subheader("😊 Mood Tracker")
st.text_area("Write about your mood today:")

# Travel List
st.subheader("✈️ Travel List")
st.text_area("Places I want to visit:")

# To-Do List
st.subheader("✅ To-Do List")
st.text_area("Tasks for today:")

# Top 5 Goals
st.subheader("🎯 Top 5 Goals")
goals = [st.text_input(f"Goal {i+1}") for i in range(5)]

# Reminders
st.subheader("⏰ Reminders")
st.text_area("Don't forget:")

# Shopping List
st.subheader("🛍️ Shopping List")
st.text_area("Items to buy:")

# Skin Care Tracker
st.subheader("💆 Skin Care Tracker")
st.text_area("Today's skin care routine:")

# Meal Plan
st.subheader("🍽️ Meal Plan")
st.text_area("What I plan to eat today:")

# Letter to My Future Self
st.subheader("💌 A Letter to My Future Self")
st.text_area("Write a letter to yourself:")

# Budget Plan and Monthly Expenses
st.subheader("💰 Budget & Expenses")
st.text_area("Track your spending:")

# Vision Board (Upload Images)
st.subheader("🎨 Vision Board")
st.file_uploader("Upload images for your vision board:", type=["jpg", "png", "jpeg"])

# Monthly Calendar
st.subheader("📅 Monthly Calendar")
st.date_input("Select a date:", datetime.date.today())

# Positive Affirmations
st.subheader("🌟 Positive Affirmations")
st.text_area("Write affirmations for yourself:")

st.success("Your journal is saved! Keep coming back to reflect and grow.")
