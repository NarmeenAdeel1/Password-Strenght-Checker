import re
import streamlit as st

# Styling
st.set_page_config(page_title="🔒 Password Strength Checker", page_icon="🛡️", layout="centered", initial_sidebar_state="expanded")

# CSS for Shimmery Effect & Styling
st.markdown(""" 
<style>
    /* Full Page Animated Shimmery Background */
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #FFD700, #FF8C00, #DAA520) !important;
        background-size: 400% 400%;
        animation: shimmer 6s infinite alternate;
        color: white !important;
        height: 100vh;
        margin: 0;
        padding: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
    }

    @keyframes shimmer {
        0% { background-position: left; }
        100% { background-position: right; }
    }

    /* Centering Everything */
    .main {text-align: center;}

    /* Input Box Styling */
    .stTextInput > div > div > input {
        width: 70% !important;
        margin: auto;
        border: 2px solid #FFD700;
        padding: 12px;
        border-radius: 10px;
        font-size: 18px;
        text-align: center;
        background-color: #fff;
        color: black;
    }

    /* Button Styling */
    div.stButton > button {
        width: 60% !important;
        background: linear-gradient(90deg, #DAA520, #FF8C00) !important;
        color: white !important;
        font-size: 20px !important;
        border-radius: 10px !important;
        padding: 12px !important;
        border: none !important;
        transition: 0.3s ease-in-out;
    }
    div.stButton > button:hover {
        background: linear-gradient(90deg, #FF8C00, #DAA520) !important;
        transform: scale(1.05);
        box-shadow: 0px 0px 15px rgba(255, 215, 0, 0.8);
    }
</style>
""", unsafe_allow_html=True)

# Page Title with Emoji
st.title("🔏 Password Strength Checker")
st.write("✨ Enter Your Password Below to Check its Strength Level! ✨")

# Function to Check Password Strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password must be at least **8 characters** long")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔡 Password must contain **both upper and lower case** characters")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔢 Password must contain at least **one digit**")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("🔣 Password must contain at least **one special character**")

    # Displaying the result
    if score == 4:
        st.success("✅ Strong Password! 🔥")
    elif score == 3:
        st.info("⚠️ Medium Password! Can be stronger 💪")
    else:
        st.error("🚨 Weak Password! Try making it stronger 🚀")

    # Feedback for improvement
    if feedback:
        with st.expander("🛠️ Improve Your Password:"):
            for feed in feedback:
                st.write(feed)

# Input and Button
password = st.text_input("🔑 Enter your password:", type="password", help="ℹ️ Ensure your password is at least **8 characters** long, contains both **upper & lower case**, at least **one digit**, and **one special character**.")

if st.button("🔍 Check Strength"):
    check_password_strength(password)
