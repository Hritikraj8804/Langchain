
### 🔹 Code Walkthrough

```python
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",   # Hugging Face model (instruction-tuned)
    task="text-generation"           # Task is text generation
)
```

* Loads **Gemma 2B IT** model from Hugging Face Inference API.
* `task="text-generation"` means it expects input text → outputs generated text.

---

```python
model = ChatHuggingFace(llm=llm)
```

* Wraps the LLM into a **Chat interface**, so it can work in LangChain pipelines.

---

```python
parser = JsonOutputParser()
```

* Tells LangChain that the output must be **valid JSON**.
* Later, the LLM will be guided to return facts in JSON format.

---

```python
template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)
```

* `PromptTemplate` defines how you ask the model.
* It has one variable: `{topic}`.
* `parser.get_format_instructions()` tells the model *how to format output as JSON*.
  Example: It will include something like

  ```json
  {
    "facts": ["...", "..."]
  }
  ```

---

```python
chain = template | model | parser
```

* Creates a **chain** where:

  1. `template` → formats the input.
  2. `model` → generates text using Gemma.
  3. `parser` → parses model’s output into JSON safely.

---

```python
result = chain.invoke({'topic':'black hole'})
print(result)
```

* Invokes the chain with `"black hole"` as the topic.
* Output will be a Python dict parsed from JSON, e.g.:

  ```python
  {
    "facts": [
      "A black hole is a region of spacetime where gravity is so strong that nothing can escape.",
      "The boundary around a black hole is called the event horizon.",
      "Black holes are formed from the collapse of massive stars.",
      "They can grow by absorbing matter and merging with other black holes.",
      "Supermassive black holes exist at the centers of most galaxies."
    ]
  }
  ```

---

### 🔹 Why This Setup is Nice

* ✅ Uses **Gemma** via Hugging Face Hub (no local install needed).
* ✅ Forces **structured JSON output**, which is reliable for apps.
* ✅ Composable with other chains (summarizers, validators, etc.).

---



<img width="1372" height="256" alt="image" src="https://github.com/user-attachments/assets/86e679f1-5cfa-47d5-977e-f7c9bc1a7289" />
