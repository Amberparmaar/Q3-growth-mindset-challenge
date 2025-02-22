import streamlit as st

# Page config
st.set_page_config(page_title="Growth mindset project", page_icon="⭐")

# Custom CSS for styling
st.markdown("""
    <style>
        /* Change background color */
        .stApp {
            background-color: #f4f4f4;
        }

        /* Title and headers */
        h1, h2, h3 {
            color: #FF5733;
            font-family: 'Arial', sans-serif;
        }

        /* Text content */
        p {
            color: #333333;
            font-family: 'Verdana', sans-serif;
            font-size: 16px;
        }

        /* Custom styling for text areas */
        div[data-baseweb="textarea"] textarea {
            background-color: #fffaf0 !important;
            color: #333 !important;
            font-family: 'Courier New', monospace !important;
            border: 2px solid #FF5733 !important;
            border-radius: 5px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title & description
st.title("🌱 Growth mindset challenge By Amber Parmaar")
st.header("Welcome to your Growth Mindset Project")
st.write("Embrace the challenge, learn from your mistakes, and grow from them. This is a project to help you develop a growth mindset.")

st.markdown("---")

# Quote section
st.header("🌑 Today's wisdom on personal growth")
st.write("'Neither success nor failure defines you; your determination to move forward does.' - Unknown")

st.markdown("---")

# User input section
st.header("💪 How are you challenging yourself today?")
user_input = st.text_area("Share your goals and progress below.")

if user_input:
    st.success(f"You are facing: {user_input}. Keep pushing forward toward your goals! 🚀")
else:
    st.warning("Tell us about your challenge to get started! 🌟")

st.markdown("---")

# Reflection section
st.header("Reflect on your progress")
st.write("Take a moment to reflect on your progress and what you've learned from your experiences.")
reflection = st.text_area("What have you learned from your challenges today?")

if reflection:
    st.success(f"Great insight! You've learned: {reflection} 🌟")
else:
    st.info("Share your reflection to continue growing! 🌱")

st.markdown("---")

# Achievements section
st.header("🏆 Celebrate your achievements")
achievement = st.text_area("What have you accomplished today?")

if achievement:
    st.success(f"Congratulations on your achievement: {achievement} 🎉")
else:
    st.info("Share your achievements to celebrate your growth! 🌟")

st.markdown("---")

# Footer
st.write("----")
st.write("Keep up the great work! 🌟")
st.write("**Created with ❤️ by Amber Parmaar**")
st.write("Find me on [LinkedIn](https://www.linkedin.com/in/amber-shoukat-19724a293/)") 
