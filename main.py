from langchain_ollama import ChatOllama

# Instantiation
llm = ChatOllama(
    model="gemma:2b",
    temperature=0,
    timeout=300,
)

# invocation
msg = [
    (
        "system",
        "You are a helpful assistant that gives proper and accurate responses. "
        "Be kind and give detailed answers.",
    ),
    ("human", "who is the latest Iran president."),
]
response = llm.invoke(msg)

print(response.content)