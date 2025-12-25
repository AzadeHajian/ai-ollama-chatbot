from langchain_ollama import ChatOllama


if __name__ == "__main__":
    # Instantiation
    llm = ChatOllama(
        model="gemma:2b",
        temperature=0,
        timeout=300,
    )

    # Initialize conversation history with system message
    conversation_history = [
        (
            "system",
            "You are a helpful assistant that gives proper and accurate responses. "
            "Be kind and give detailed answers.",
        )
    ]

    print("Chatbot is ready. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        
        # Add user message to history
        conversation_history.append(("human", user_input))
        
        # Invoke with full conversation history
        response = llm.invoke(conversation_history)
        
        # Add assistant response to history
        conversation_history.append(("assistant", response.content))
        
        print(f"Assistant: {response.content}")