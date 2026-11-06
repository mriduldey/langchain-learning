# Lesson 03: LangChain Expression Language (LCEL)

## What this lesson is teaching

This lesson introduces the core idea behind LangChain Expression Language (LCEL): building AI pipelines by composing small components into a chain using the `|` operator.

Instead of writing messy imperative code such as:

```python
result = model.invoke(prompt)
parsed = parser.parse(result)
```

LCEL lets you express the same logic in a clean, composable way:

```python
chain = prompt | model | parser
result = chain.invoke({"topic": "LangChain"})
```

The lesson focuses on three important patterns:

- `RunnableLambda`: wrap a Python function as a runnable step
- chaining with `|`: connect runnable components in sequence
- `RunnableParallel`: run multiple branches at the same time

This is one of the most important concepts in LangChain because it makes AI workflows feel like normal Python pipelines instead of one-off scripts.

## Why this is needed

Real LLM applications are rarely a single call to a model. They often involve a sequence like this:

1. Build a prompt
2. Send it to a model
3. Parse the output
4. Maybe transform the output
5. Send additional data to another model or tool

Without a structured pattern, this becomes hard to manage, hard to test, and hard to reuse.

LCEL solves this problem by giving us a standard way to connect components. The benefits are:

- readability: each step is clear and composable
- reuse: the same prompt or parser can be used in multiple chains
- modularity: you can swap models or formatting steps with minimal changes
- parallelism: you can execute multiple tasks at once
- consistency: all LangChain components follow the same runnable interface

In short, LCEL is the foundation for building production-ready LLM pipelines.

## The big idea: everything is a runnable

In LangChain, many objects are "runnables." A runnable is simply something that can:

- accept an input
- process it
- return an output

Examples include:

- prompts
- chat models
- output parsers
- custom Python functions wrapped in `RunnableLambda`
- chains made by combining runnables

The `|` operator is what lets us compose these pieces together.

```python
chain = prompt | model | parser
```

This means:

- prompt produces input for the model
- model produces raw output
- parser turns that raw output into a clean Python value

## File walkthrough

### 1. `1.runnable_lambda.py`

This file introduces the simplest form of LCEL composition:

```python
from langchain_core.runnables import RunnableLambda

add_five = RunnableLambda(
    lambda x: x + 5
)

multiply_5 = RunnableLambda(
    lambda x: x * 5
)

chain = add_five | multiply_5

result = chain.invoke(5)
print(result)
```

What happens here?

- `add_five` takes an input and adds 5
- `multiply_5` takes the output of `add_five` and multiplies it by 5
- `chain = add_five | multiply_5` creates a pipeline
- `chain.invoke(5)` runs the pipeline with input `5`

Step by step:

1. Input is `5`
2. `add_five` runs: `5 + 5 = 10`
3. `multiply_5` runs: `10 * 5 = 50`
4. Final result is `50`

This is a great beginner example because it shows the exact idea behind LCEL without needing an LLM yet.

### 2. `2.runnable_lambda_real_use.py`

This file moves from a mathematical example to a real LLM workflow.

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_learning.common.main import get_llm

model = get_llm()
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a senior Python instructor. Keep explanations concise."
    ),
    (
        "human",
        "Explain {topic} with one example."
    )
])

parser = StrOutputParser()

chain = prompt | model | parser
```

Here, the pieces are:

- `ChatPromptTemplate`: builds the prompt message structure
- `model`: the LLM we call
- `StrOutputParser`: converts the model output into plain text

The key observation is that the chain is still just a composition of runnables:

```python
prompt | model | parser
```

This is how real LCEL-based LLM apps are built.

The example uses:

```python
for chunk in chain.stream({"topic": "Langchain"}):
    print(chunk, end="", flush=True)
```

This is important because `stream()` emits output incrementally instead of waiting for the entire response. It is useful for chat interfaces, progress display, and streaming responses in real apps.

### 3. `3.runnable_parallel.py`

This file introduces parallel execution.

```python
parallel_chain = RunnableParallel(
    beginner=beginner_chain,
    advanced=advanced_chain
)

result = parallel_chain.invoke({
    "topic": "Python decorators"
})
```

This uses two different prompts:

- one for a beginner audience
- one for a senior engineer audience

Both are run at the same time, and the result is returned as a dictionary:

```python
{
    "beginner": "...",
    "advanced": "..."
}
```

This is useful when you want to:

- compare different explanations
- run parallel queries for different audiences
- gather multiple perspectives at the same time

The main idea is that `RunnableParallel` lets you branch your workflow instead of doing everything sequentially.

## Example walkthrough

Let us walk through the same pattern in a simple way.

### Example 1: simple lambda pipeline

```python
chain = add_five | multiply_5
result = chain.invoke(5)
```

The execution flow is:

```text
5
  -> add_five -> 10
  -> multiply_5 -> 50
```

Final output:

```python
50
```

### Example 2: model pipeline

```python
chain = prompt | model | parser
response = chain.invoke({"topic": "LangChain"})
```

The execution flow is:

```text
{"topic": "LangChain"}
  -> prompt template
  -> LLM model
  -> StrOutputParser
  -> final text response
```

This is the basic production pattern used in real LangChain applications.

### Example 3: parallel pipeline

```python
result = parallel_chain.invoke({"topic": "Python decorators"})
print(result["beginner"])
print(result["advanced"])
```

The system runs both branches concurrently:

```text
Input: {"topic": "Python decorators"}

beginner branch  -> beginner_prompt -> model -> parser
advanced branch  -> advanced_prompt -> model -> parser
```

Then it returns both results together.

## Why this matters in practice

The pattern you learn in this lesson is used across many AI applications:

- chat assistants with prompt templates
- document Q&A pipelines
- summarization workflows
- multi-step agent systems
- retrieval and generation pipelines
- branching logic for different user personas or outputs

Once you can think in terms of runnables and composition, you can build more powerful systems without writing fragile custom orchestration code.

## Summary

Lesson 03 teaches the heart of LangChain's compositional design.

The most important ideas are:

- everything can be a runnable
- runnables can be combined with `|`
- `RunnableLambda` wraps Python logic
- `RunnableParallel` runs branches simultaneously
- LCEL makes AI pipelines readable, reusable, and modular

In one sentence:

LCEL lets you treat LLM workflows like normal Python pipelines, where inputs flow through a series of intelligent steps and the output is assembled in a clean, composable way.

This is the foundation for almost everything you build with LangChain after the basics.
