from langchain_core.prompts import ChatPromptTemplate

from langchain_learning.common.main import get_llm

prompt = ChatPromptTemplate.from_messages([
    (
        "system", 
        "You are a helpful assistant that translates {input_language} text to {output_language} font."
        "You are language expert and you know both {input_language} and {output_language} very well."
    ),
    (
        "user",
        "Translate the following text from {input_language} text to {output_language} text: {text}",
    )
])

prompt_result = prompt.invoke({
    "input_language": "English",
    "output_language": "Bengali",
    "text": "I am a software engineer. What do you do?"
})

for message in prompt_result.messages:
    print(message.type, ":", message.content)
    

model = get_llm()
for chunk in model.stream(prompt_result):
        print(chunk.text, end="", flush=True)