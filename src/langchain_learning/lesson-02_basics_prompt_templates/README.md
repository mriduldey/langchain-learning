# Lesson 02: Basics of Prompt Templates in LangChain

## What this lesson is teaching

This lesson introduces prompt templates, which are one of the most important building blocks in LangChain.

A prompt template is a reusable prompt structure where some parts are fixed and some parts are filled dynamically at runtime. Instead of manually building strings with Python `f`-strings every time, LangChain gives you a cleaner and more structured way to define prompts.

In this lesson, we learn how to:

- create simple text prompts with `PromptTemplate`
- create chat prompts with `ChatPromptTemplate`
- pass dynamic values into the prompt
- partially fill some variables using `.partial()`
- include conversation history using `MessagesPlaceholder`

This is the step where LLM applications stop being ad-hoc scripts and start becoming reusable, maintainable systems.

## Why this is needed

If you write prompts directly as raw strings, you quickly run into a few problems:

- the same prompt structure is repeated across many calls
- prompt variables are hard to manage and validate
- system instructions and user input get mixed together
- chat history is difficult to insert cleanly
- it is harder to reuse prompts in different parts of an application

Prompt templates solve these problems by separating:

- fixed instructions
- dynamic variables
- message structure
- conversation context

That makes your LLM code easier to read, test, and scale.

In real applications, prompts are rarely static. You usually need to inject values such as:

- `{topic}`
- `{language}`
- `{text}`
- `{history}`
- `{question}`

Prompt templates give you a clean, standardized way to do this.

## The big idea

The main idea is simple:

1. define a prompt structure
2. mark dynamic placeholders
3. pass input values at runtime
4. send the completed prompt to the model

LangChain handles the formatting for you, and it supports both simple text prompts and messages-based chat prompts.

## File walkthrough

### 1. `1.prompt_template_intro.py`

This file explains the motivation behind prompt templates.

It starts with a plain Python function that builds a prompt using string interpolation:

```python
def explain_topic(topic, level):
    prompt = f"""
    Explain {topic} to a {level} developer.
    Include a code example.
    """
    return model.stream(prompt)
```

This works, but it is not a robust pattern for production because:

- prompt logic is embedded in Python code
- it is hard to reuse across many calls
- instructions and variables are mixed manually
- there is no standard prompt structure for chat-based applications

The comments in the file clearly explain the real value of LangChain prompt templates:

- separating system instructions from user inputs
- automatically identifying required variables
- supplying predefined configuration values
- inserting conversation history
- integrating with the rest of the LangChain runtime

This file is the conceptual bridge between raw Python prompting and structured LangChain prompts.

### 2. `2.prompt_template.py`

This file introduces `PromptTemplate`, which is used for simple text prompts.

```python
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    "Explain {topic} to a {level} developer."
)

result = prompt.invoke({
    "topic": "langchain",
    "level": "junior"
})

print(result.to_string())
```

This tells LangChain:

- the template is a string with placeholders
- `{topic}` and `{level}` are variables to fill at runtime
- `invoke()` provides the values

The prompt template then renders a final string, which can be passed to a model.

This is the easiest way to understand prompt templates because the input is just a plain string.

### 3. `3.chat_prompt_template.py`

This file introduces the more common chat-based prompt structure using `ChatPromptTemplate`.

```python
from langchain_core.prompts import ChatPromptTemplate

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
```

This is a major step up from simple `PromptTemplate` because chat prompts are structured as a sequence of messages.

Unlike a plain text prompt, a chat prompt often separates:

- system instructions
- user input
- variables for translation or formatting

This pattern is much closer to how real chat assistants are built.

The example then invokes the template with values like:

```python
{
    "input_language": "English",
    "output_language": "Bengali",
    "text": "I am a software engineer. What do you do?"
}
```

After rendering, the prompt is passed to the model for generation.

This file is important because real LLM apps almost always use chat-style prompts rather than a single flat string.

### 4. `4.partial_prompt.py`

This file introduces `.partial()`, which lets you pre-fill some variables in the prompt template.

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a {language} instructor."),
    ("human", "Explain {topic}.")
])

python_prompt = prompt.partial(language="Python")
```

Now the prompt already knows the `language` value, so the user only needs to provide `{topic}`:

```python
result = python_prompt.invoke({"topic": "decorators"})
```

This is useful when a value is repeated many times across prompts, such as:

- language
- role
- domain
- company style
- default instructions

`partial()` reduces duplication and keeps prompts cleaner.

### 5. `5.messages_placeholder.py`

This file introduces `MessagesPlaceholder`, which is used for conversation history.

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder("history"),
    ("human", "{question}")
])
```

The template includes a placeholder for prior chat messages, such as:

```python
history = [
    HumanMessage(content="My favorite language is Python."),
    AIMessage(content="Understood.")
]
```

Then the final invocation includes both the history and the current question:

```python
prompt.invoke({
    "history": history,
    "question": "What is my favorite language?"
})
```

This is essential for chatbots and assistant-style apps because the model needs context from previous messages.

Without a placeholder for history, the model would treat each request as a brand-new conversation.

## Example walkthrough

Let us walk through the main pattern using a simple example.

### Example 1: plain prompt template

```python
prompt = PromptTemplate.from_template(
    "Explain {topic} to a {level} developer."
)

result = prompt.invoke({
    "topic": "langchain",
    "level": "junior"
})
```

The template renders into something like:

```text
Explain langchain to a junior developer.
```

Then this final string is sent to the model.

### Example 2: chat prompt template

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Explain {topic} in simple terms.")
])

result = prompt.invoke({"topic": "Python decorators"})
```

This becomes a chat message sequence with:

- a system message
- a human message containing the final question

This matches how modern LLM APIs expect prompts to be structured.

### Example 3: partial prompt

```python
python_prompt = prompt.partial(language="Python")
result = python_prompt.invoke({"topic": "decorators"})
```

This is cleaner because you do not have to pass `language="Python"` every time.

### Example 4: prompt with history

```python
prompt.invoke({
    "history": history,
    "question": "What is my favorite language?"
})
```

The model sees both earlier messages and the current question, so it can respond in context.

## Why this matters in practice

Prompt templates are not just a convenience feature; they are a core part of building strong LLM applications.

They help you:

- define reproducible prompts
- maintain consistent behavior across repeated calls
- separate prompt logic from Python business logic
- handle multi-turn conversations properly
- reuse templates across many parts of an app

This is especially important when you move from experimentation to real-world systems, where clean prompt management matters a lot.

## Summary

Lesson 02 teaches the foundation for working with prompts in LangChain.

The most important ideas are:

- prompt templates make prompts reusable and structured
- `PromptTemplate` is for text-based prompts
- `ChatPromptTemplate` is for message-based chat prompts
- `.partial()` lets you fix some values ahead of time
- `MessagesPlaceholder` allows conversation history to be included

In one sentence:

Prompt templates are the way LangChain turns dynamic user input, instructions, and previous conversation into a clean, reusable prompt sent to an LLM.

This lesson is the bridge between basic model usage and real LangChain applications, because most practical AI workflows depend on structured prompts rather than raw strings.
