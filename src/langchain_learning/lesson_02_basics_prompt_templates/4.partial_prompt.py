from langchain_core.prompts import ChatPromptTemplate

from langchain_learning.common.main import get_llm

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a {language} instructor."),
    ("human", "Explain {topic}.")
])

#partial() returns a new template with some variables already supplied.
python_prompt = prompt.partial(language="Python")

result = python_prompt.invoke({"topic": "decorators"})

model = get_llm()
for chunk in model.stream(result):
    print(chunk.text, end="", flush=True)
