from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    "Explain {topic} to a {level} developer."
)

result = prompt.invoke({
    "topic": "langchain",
    "level": "junior"
})

print(prompt)
print(result.to_string())