

### 1. **Model Setup**

```python
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
```

* You’re using the HuggingFace model **Gemma-2-2B-IT** for **text generation**.
* `ChatHuggingFace` wraps it so it works like a conversational LLM in LangChain.

---

### 2. **Prompt Templates**

```python
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)
```

* **template1**: Generates a **detailed report** about a given topic.
* **template2**: Takes text and asks the model to produce a **5-line summary**.

⚠️ Small issue: You wrote `"/n"` instead of `"\n"`.

* `"/n"` = literal string `/n`.
* `"\n"` = newline (correct).
  So you should fix it like this:

```python
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text.\n{text}',
    input_variables=['text']
)
```

---

### 3. **Generate Report**

```python
prompt1 = template1.invoke({'topic':'black hole'})
result = model.invoke(prompt1)
```

* `template1.invoke()` → creates a prompt:
  `"Write a detailed report on black hole"`.
* `model.invoke(prompt1)` → sends that to the model → gets a **long detailed response** about black holes.

---

### 4. **Summarize the Report**

```python
prompt2 = template2.invoke({'text':result.content})
result1 = model.invoke(prompt2)
```

* `template2.invoke()` → creates a summary prompt:
  `"Write a 5 line summary on the following text.\n <detailed black hole report>"`.
* `model.invoke(prompt2)` → sends it to the model → gets a **short summary** (5 lines).

---

### 5. **Print Final Summary**

```python
print(result1.content)
```

* Displays the **summary** of the report.

---

✅ **So overall flow is:**

1. Ask the model for a detailed report.
2. Take that report, feed it into a summary prompt.
3. Get a concise summary (5 lines).

---



<img width="1201" height="290" alt="image" src="https://github.com/user-attachments/assets/698661e0-e835-4794-af7e-30004a1eccb0" />
