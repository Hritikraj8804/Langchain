
## 🔹 Step 1: Load the Model

```python
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)
```

* This connects to the **Gemma-2-2B-Instruct model** on HuggingFace.
* `ChatHuggingFace` wraps the LLM so we can use it inside LangChain pipelines.

---

## 🔹 Step 2: Define Prompts

```python
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)
```

* First prompt → asks the model to generate a **long report** on the given `{topic}`.

```python
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text:\n{text}',
    input_variables=['text']
)
```

* Second prompt → asks the model to generate a **5-line summary** from some `{text}`.

---

## 🔹 Step 3: Parser

```python
parser = StrOutputParser()
```

* This takes the **raw LLM output** (which might include extra metadata) and converts it into a **plain string** so we can feed it to the next step.

---

## 🔹 Step 4: Define the Chain

```python
chain = RunnableSequence(
    first = template1 | model | parser,
    middle = (lambda x: {"text": x}) | template2 | model | parser
)
```

Here’s the magic ✨:

1. `template1 | model | parser`

   * Takes input `{"topic": "black hole"}`
   * Generates a **detailed report** (string).

2. `(lambda x: {"text": x})`

   * Converts that string into a dictionary like `{"text": "...report..."}`
   * This is required because `template2` expects `{text}` as input.

3. `template2 | model | parser`

   * Uses the dictionary from step 2 to run the summary prompt.
   * Model outputs a **5-line summary** string.

So effectively, it’s a **two-step pipeline**:

```
topic -> detailed report -> summary of that report
```

---

## 🔹 Step 5: Run the Chain

```python
result = chain.invoke({"topic": "black hole"})
print(result)
```

* Input: `{"topic": "black hole"}`
* Output: a **5-line summary of the generated report** on black holes.

---

✅ **In short**:

1. Generate a detailed report.
2. Pass it as input to another prompt.
3. Summarize in 5 lines.

---



<img width="1342" height="286" alt="image" src="https://github.com/user-attachments/assets/12bd7267-3895-411e-ba7e-894bf0fa97d7" />
