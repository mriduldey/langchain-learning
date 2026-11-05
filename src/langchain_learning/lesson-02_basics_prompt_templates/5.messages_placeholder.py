from langchain_core.prompts import ( ChatPromptTemplate, MessagesPlaceholder )
from langchain_core.messages import ( HumanMessage, AIMessage)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder("history"),
    ("human", "{question}")
])

history = [
    HumanMessage(
        content="My favorite language is Python."
    ),
    AIMessage(
        content="Understood."
    )
]

result = prompt.invoke({
    "history": history,
    "question": "What is my favorite language?"
})


for message in result.messages:
    print(message.type, message.content)

# output:
# system You are a helpful assistant.
# human My favorite language is Python.
# ai Understood.
# human What is my favorite language?