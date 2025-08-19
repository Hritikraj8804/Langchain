
### **1. Define Prompts**

```python
prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)
```

* This will **generate a long detailed report** on the given `topic`.
* Example input: `"Russia vs Ukraine"`
* Example output: *a long essay-like response*.

```python
prompt2 = PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
)
```

* This is for **summarizing text** (used later when report is too long).

---

### **2. Model + Parser**

```python
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
parser = StrOutputParser()
```

* `model`: Uses **Gemini 1.5 Flash** to generate text.
* `parser`: Ensures the output is returned as a clean string.

---

### **3. Report Generation Chain**

```python
report_gen_chain = prompt1 | model | parser
```

* Pipeline:
  `topic` → `prompt1` → `model` → `parser`
* Example: Input `"Russia vs Ukraine"`
  Output → A long detailed report string.

---

### **4. Branching Logic**

```python
branch_chain = RunnableBranch(
    (lambda x: len(x.split())>300, prompt2 | model | parser),
    RunnablePassthrough()
)
```

* `RunnableBranch` works like an **if-else condition** for chains:

  * If the text length `> 300 words` → summarize using `prompt2`.
  * Else → return the text as-is (no change).

---

### **5. Final Pipeline**

```python
final_chain = RunnableSequence(report_gen_chain, branch_chain)
```

* Step 1: Generate a **detailed report**.
* Step 2: Check word length:

  * If too long (>300 words) → summarize it.
  * Otherwise → return the original report.

---

### **6. Invocation**

```python
print(final_chain.invoke({'topic':'Russia vs Ukraine'}))
```

* Input: `{'topic':'Russia vs Ukraine'}`
* Flow:

  1. `prompt1` creates a detailed report.
  2. If the report is very long → `prompt2` summarizes it.
  3. Otherwise → returns the detailed report directly.

---

✅ **In short**:
This pipeline generates a detailed report on `"Russia vs Ukraine"`. If the report is too long (>300 words), it automatically summarizes it, otherwise it keeps it unchanged.

---


<img width="1311" height="208" alt="image" src="https://github.com/user-attachments/assets/44247da8-afae-48a4-baba-a77c3cb32bd1" />
