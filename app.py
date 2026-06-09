import streamlit as st
import requests

# Page Config
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Sidebar
with st.sidebar:
    st.title("🤖 AI Chatbot")
    st.write("Powered by Llama 3")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Main Title
st.title("💬 AI Chatbot")

st.caption("Ask anything and get AI-powered responses.")

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
prompt = st.chat_input("Type your question here...")

if prompt:

    # Display User Message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            try:
                response = requests.post(
                    "http://localhost:11434/api/generate",
                    json={
                        "model": "llama3",
                        "prompt": prompt,
                        "stream": False
                    }
                )

                result = response.json()
                ai_response = result["response"]

                st.markdown(ai_response)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": ai_response
                    }
                )

            except Exception as e:
                st.error(
                    "Unable to connect to Ollama. Make sure Ollama is running."
                )
                st.write(str(e))