import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai   # ✅ সঠিক import

# --- Page Config ---
st.set_page_config(
    page_title="Gemini 2.5 Flash Chatbot",
    page_icon="🧠",
    layout="wide",
)

# --- Custom Dark Theme CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

    html, body, [class^='css'] {
        font-family: 'Roboto', Arial, sans-serif !important;
        background-color: #121212;
        color: #e0e0e0;
    }
    .main {
        background-color: #121212;
    }
    .stChatMessage.user {
        background: linear-gradient(90deg, #4e54c8 0%, #8f94fb 100%);
        color: #ffffff;
        border-radius: 12px;
        margin-bottom: 12px;
        font-family: 'Roboto', Arial, sans-serif !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
    }
    .stChatMessage.assistant {
        background: linear-gradient(90deg, #ff9966 0%, #ff5e62 100%);
        color: #ffffff;
        border-radius: 12px;
        margin-bottom: 12px;
        font-family: 'Roboto', Arial, sans-serif !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
    }
    .stTextInput>div>input {
        border-radius: 8px;
        border: 1px solid #ff4e50;
        font-family: 'Roboto', Arial, sans-serif !important;
        background: #1e1e1e;
        color: #ffffff;
    }
    h1, h2, h3, h4, h5, h6, p {
        color: #e0e0e0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Font description ---
st.markdown("<p style='text-align:center; color:#b0b0b0; font-size:15px;'>Font family used: <b>Roboto</b> (with fallback to Arial, sans-serif)</p>", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6e/Gemini_logo.png", width=120)
    st.markdown("## Gemini 2.5 Flash Chatbot")
    st.info("Talk to Google's Gemini AI model in Bengali or English!")
    st.markdown("---")
    st.write("👨‍💻 Made by: **MD Uzzal Mia**")

# --- Load environment variables ---
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.error("")
else:
    genai.configure(api_key=GOOGLE_API_KEY)

# --- Initialize Gemini model ---
model = genai.GenerativeModel("gemini-2.5-flash")

# --- Chat history ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- Main Chat UI ---
st.markdown("<h1 style='text-align:center; color:#90caf9;'>🧠 Gemini 2.5 Flash Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#bdbdbd;'>Ask anything in Bengali or English!</p>", unsafe_allow_html=True)

chat_container = st.container()
with chat_container:
    for chat in st.session_state.chat_history:
        with st.chat_message(chat["role"]):
            st.markdown(chat["content"])

# --- Chat input ---
user_prompt = st.chat_input("আপনার প্রশ্ন লিখুন... | Type your question...")
if user_prompt:
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)
    with st.spinner("Gemini is thinking..."):
        try:
            response = model.generate_content(user_prompt)  # ✅ Updated
            st.session_state.chat_history.append({"role": "assistant", "content": response.text})
            with st.chat_message("assistant"):
                st.markdown(response.text)
        except Exception as e:
            st.error(f"Error: {str(e)}")
