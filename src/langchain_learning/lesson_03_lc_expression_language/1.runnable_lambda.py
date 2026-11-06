from langchain_core.runnables import RunnableLambda

add_five = RunnableLambda(
    lambda x: x + 5
)

multiply_5 = RunnableLambda(
    lambda x: x * 5
)

chain = add_five | multiply_5

result = chain.invoke(5)

print(result)  # Output: 50