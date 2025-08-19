It’s basically a **two-step pipeline**:

1. **Step 1** → Generate a joke about some topic (e.g., AI).
2. **Step 2** → Take that joke and explain why it’s funny.

---

## **Step-by-step**

### **1. Prompt 1 → Write a joke**

```python
prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)
```

* If you give `topic="AI"`, it becomes:

```
Write a joke about AI
```

---

### **2. Model → Generate**

```python
gemini_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
```

* Uses Google **Gemini 1.5 Flash** to answer.
* So it might write:

```
Why did the AI go to therapy?  
Because it had too many deep learning issues!
```

---

### **3. Parser → Clean text**

```python
parser = StrOutputParser()
```

* Makes sure we only keep the **string output**.

---

### **4. Prompt 2 → Explain the joke**

```python
prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)
```

* Takes the joke and asks:

```
Explain the following joke - Why did the AI go to therapy? Because it had too many deep learning issues!
```

---

### **5. Model again**

* Gemini explains it, e.g.:

```
The joke is funny because "deep learning" is an AI technique, but here it's used as a pun meaning emotional issues.
```

---

### **6. RunnableSequence**

```python
chain = RunnableSequence(prompt1, gemini_model, parser, prompt2, gemini_model, parser)
```

* This is a straight **pipeline**:

```
Topic → [Prompt1] → [Gemini] → [Parser] → [Prompt2] → [Gemini] → [Parser] → Final Answer
```

---

### **7. Run it**

```python
print(chain.invoke({'topic':'AI'}))
```

* First → Gemini writes a joke about AI.
* Then → Gemini explains its own joke.
* Final output = **explanation of the joke**.

---

✅ So you’re chaining Gemini **twice**:

1. To **create humor**,
2. To **analyze humor**.



<img width="1185" height="218" alt="image" src="https://github.com/user-attachments/assets/aca3bd54-863e-49c6-848b-7eb243aa8752" />
