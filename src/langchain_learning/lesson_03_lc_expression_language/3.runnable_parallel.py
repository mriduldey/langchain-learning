from langchain_core.runnables import RunnableParallel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_learning.common.main import get_llm

model = get_llm()

parser = StrOutputParser()

beginner_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} for a beginner."
)

advanced_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} for a senior engineer."
)

beginner_chain = (
    beginner_prompt | model | parser
)

advanced_chain = (
    advanced_prompt | model | parser
)

parallel_chain = RunnableParallel(
    beginner=beginner_chain,
    advanced=advanced_chain
)

result = parallel_chain.invoke({
    "topic": "Python decorators"
})

print(result["beginner"])
print(result["advanced"])