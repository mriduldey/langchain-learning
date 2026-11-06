from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_learning.common.main import get_llm

model = get_llm()

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a senior Python instructor. "
        "Keep explanations concise."
    ),
    (
        "human",
        "Explain {topic} with one example."
    )
])

# StrOutputParser converts the AI's response into a plain Python string.
# Without it, the model typically returns an AIMessage object.
parser = StrOutputParser()

# LCEL (LangChain Expression Language) connects Runnables using the | operator.
# Each component's output becomes the next component's input.
chain = prompt | model | parser


# result = chain.invoke({"topic": "LangChain"})

# print(result)

# stream() yields text chunks incrementally instead of waiting for the full response.
# flush=True displays each chunk immediately without buffering.
for chunk in chain.stream({"topic": "Langchain"}):
    print(chunk, end="", flush=True)