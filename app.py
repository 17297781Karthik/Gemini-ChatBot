from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai

# Configure Gemini
os.getenv("Google_api_key")
genai.configure(api_key=os.getenv("Google_api_key"))

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

# Page config with custom theme

st.set_page_config(
    page_title="Gemini Chat",
    page_icon="🤖",
    layout="centered"
)


st.markdown("""
<style>
.stTextArea textarea {
    font-size: 16px !important;
    border-radius: 10px;
}
.main {
    padding: 2rem;
}
            
</style>
""", unsafe_allow_html=True)

st.title("💬 Gemini Chat")
# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input with keyboard handling
prompt = st.chat_input("Ask something...", key="chat_input")

if prompt:
    # Add user message to chat
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Get and display assistant response
    with st.chat_message("assistant"):
        response = get_gemini_response(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})