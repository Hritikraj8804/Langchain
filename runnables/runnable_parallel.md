
## **Step-by-step explanation**

### **1. Prompts**

```python
prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a Linkedin post about {topic}',
    input_variables=['topic']
)
```

* **Prompt 1** → asks Gemini to write a tweet (short, catchy).
* **Prompt 2** → asks Gemini to write a LinkedIn post (longer, professional).

---

### **2. Model**

```python
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash"
)
```

* Using **Gemini 1.5 Flash** (fast, lightweight model).

---

### **3. Parser**

```python
parser = StrOutputParser()
```

* Makes sure output is just **plain text**.

---

### **4. RunnableParallel**

```python
parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser)
})
```

* **RunnableParallel** → runs multiple tasks simultaneously.
* Here, two sub-chains:

  * `"tweet"` chain: Prompt1 → Model → Parser
  * `"linkedin"` chain: Prompt2 → Model → Parser

Both run **together** instead of one after another.

---

### **5. Invoke the chain**

```python
result = parallel_chain.invoke({'topic':'Japan'})
```

* Input: `topic="Japan"`
* Output: A dictionary like:

```python
{
  "tweet": "🇯🇵 From sushi to Shinkansen, Japan blends tradition with innovation! #TravelJapan #Culture",
  "linkedin": "Japan is a land of contrasts — where centuries-old traditions meet cutting-edge technology..."
}
```

---

### **6. Print results**

```python
print(result['tweet'])
print(result['linkedin'])
```

* First line → the short **Tweet**.
* Second line → the longer **LinkedIn post**.

---

✅ So this setup is great when you want **multiple types of content from the same input**.


<img width="1290" height="640" alt="image" src="https://github.com/user-attachments/assets/30308e4b-0915-417b-bc3b-af8334888e8d" />
