import streamlit as st
from langchain_ollama import ChatOllama

# Initialize conversation history in session state if not present
if "messages" not in st.session_state:
    st.session_state.messages = [
        (
            "system",
            "You are a helpful assistant that gives proper and accurate responses. "
            "Be kind and give detailed answers.",
        )
    ]

# Sidebar for controls
st.sidebar.title("🤖 Chatbot Settings")

# Model selection with icon (using emoji as icon)
model_options = ["gemma:2b", "llama2:7b", "mistral:7b"]
model = st.sidebar.selectbox("🧠 Model", model_options, index=0)

# Temperature slider
temperature = st.sidebar.slider("🌡️ Temperature", 0.0, 1.0, 0.0, 0.1)

# Timeout slider
timeout = st.sidebar.slider("⏱️ Timeout (seconds)", 10, 600, 300, 10)

# Clear chat button
if st.sidebar.button("🗑️ Clear Chat"):
    # Reset messages to only system message
    st.session_state.messages = [
        (
            "system",
            "You are a helpful assistant that gives proper and accurate responses. "
            "Be kind and give detailed answers.",
        )
    ]
    st.rerun()

# History expander
with st.sidebar.expander("📜 History"):
    for i, message in enumerate(st.session_state.messages[1:], 1):  # Skip system message
        st.write(f"{i}. **{message[0].capitalize()}**: {message[1]}")

# Initialize the LLM with selected parameters
llm = ChatOllama(
    model=model,
    temperature=temperature,
    timeout=timeout,
)

# Set page title
st.title("AI Chatbot")

# Display chat messages from history on app rerun
for message in st.session_state.messages[1:]:  # Skip the system message
    with st.chat_message(message[0]):
        st.markdown(message[1])

# Accept user input
if prompt := st.chat_input("What is your question?"):
    # Add user message to chat history
    st.session_state.messages.append(("human", prompt))
    # Display user message in chat message container
    with st.chat_message("human"):
        st.markdown(prompt)

    # Get assistant response
    response = llm.invoke(st.session_state.messages)
    # Add assistant response to chat history
    st.session_state.messages.append(("assistant", response.content))
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response.content)