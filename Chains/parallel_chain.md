## **What this code does**

You’re asking two AI models to work **at the same time** (parallel) to:

1. Make **notes** from a given text.
2. Make **quiz questions** from the same text.
   Then, you combine both into **one single document**.

---

## **Step-by-step**

### **1. Load tools & AI models**

```python
llm = HuggingFaceEndpoint(...)
model1 = ChatHuggingFace(llm=llm)  # HuggingFace Gemma model

model2 = ChatGoogleGenerativeAI(model="gemini-1.5-pro")  # Google Gemini model
```

* **model1 (Gemma)** → Writes notes & merges the final result.
* **model2 (Gemini)** → Writes quiz questions.

---

### **2. Create prompts (instructions for AI)**

```python
prompt1 = PromptTemplate(
    template='Generate short and simple notes ...',
    input_variables=['text']
)
prompt2 = PromptTemplate(
    template='Generate 5 short question answers ...',
    input_variables=['text']
)
prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document ...',
    input_variables=['notes', 'quiz']
)
```

Think of these as **three jobs**:

1. Job 1 → Summarize text into **notes**.
2. Job 2 → Make a **quiz** from text.
3. Job 3 → Merge notes + quiz into **one paper**.

---

### **3. Parse the output into clean text**

```python
parser = StrOutputParser()
```

This is like saying:

> “Hey AI, make sure I get plain text, not extra metadata.”

---

### **4. Run jobs in parallel**

```python
parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})
```

* **RunnableParallel** → Runs **two AI tasks at the same time**.
* The result will be like:

```python
{
    "notes": "...notes text...",
    "quiz": "...quiz text..."
}
```

---

### **5. Merge both outputs**

```python
merge_chain = prompt3 | model1 | parser
```

Here:

* We give notes + quiz to Gemma.
* Gemma writes a **single combined document**.

---

### **6. Build the full chain**

```python
chain = parallel_chain | merge_chain
```

Flow:

1. **parallel\_chain** → Makes notes & quiz at the same time.
2. **merge\_chain** → Combines them into one output.

---

### **7. Run it with the text**

```python
result = chain.invoke({'text': text})
```

* Input → A long explanation of Korean, Chinese, and Japanese languages.
* Output → A **study sheet** with notes + quiz merged together.

---

## **Cartoon analogy**

Imagine you’re the **teacher**:

1. You give **one chapter** to **Student A** and **Student B** at the same time.
2. **Student A (Gemma)** → Writes a summary.
3. **Student B (Gemini)** → Writes quiz questions.
4. You take both outputs and give them to **Student A** again to make a **final study handout**.

---




<img width="395" height="777" alt="image" src="https://github.com/user-attachments/assets/56bed4f7-a087-4370-9ce3-2c3d9929a09d" />

<img width="1487" height="538" alt="image" src="https://github.com/user-attachments/assets/7041b699-008f-4974-a6d1-2a12600d9a56" />

<img width="1222" height="317" alt="image" src="https://github.com/user-attachments/assets/4e4969ad-18be-4c5d-bf20-f18d1ee28ce2" />
