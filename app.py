import streamlit as st
from src.llm_manager import GeminiLLM

st.set_page_config(page_title="CareerGenie AI", page_icon="rocket")

if "llm" not in st.session_state:
    st.session_state.llm = GeminiLLM()
    st.session_state.llm.start_chat()

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.title("CareerGenie 🧞‍♂️")
    st.markdown("Your AI Partner for:")
    st.markdown("- Resume Reviews")
    st.markdown("- Interview Prep")
    st.markdown("- Career Path Planning")
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.session_state.llm.start_chat()
        st.rerun()

st.title("AI Career Advisor")
st.markdown("---")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about your resume, interview, or career path..."):

    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("Thinking..."):
        response_text = st.session_state.llm.get_response(prompt)

    with st.chat_message("assistant"):
        st.markdown(response_text)
    
    st.session_state.messages.append({"role": "assistant", "content": response_text})