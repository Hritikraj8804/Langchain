
## **Step-by-step**

### **1. Prompt to generate a joke**

```python
prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)
```

* Input: `{'topic': 'cricket'}`
* Example output:

```
Why don’t cricketers ever get sunburned?  
Because they have too many good covers!
```

---

### **2. Joke generation chain**

```python
joke_gen_chain = RunnableSequence(prompt1, model, parser)
```

* Flow:
  **Topic → Prompt → Gemini → Parser → Joke string**

Result: `"Why don’t cricketers ever get sunburned? Because they have too many good covers!"`

---

### **3. Prepare parallel branch**

```python
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})
```

* **RunnableParallel** = run multiple things at the same time.
* Two branches:

  * `'joke'`: `RunnablePassthrough()` → just passes the joke along.
  * `'explanation'`: Takes the joke → feeds it into `prompt2` → Gemini explains.

So now, instead of replacing the joke, you keep **both**:

```python
{
  "joke": "...the joke...",
  "explanation": "...Gemini’s explanation..."
}
```

---

### **4. Final chain**

```python
final_chain = RunnableSequence(joke_gen_chain, parallel_chain)
```

* First stage: **Generate the joke**.
* Second stage: **Run both joke passthrough & explanation in parallel**.

---

### **5. Run**

```python
print(final_chain.invoke({'topic':'cricket'}))
```

Example output:

```python
{
  'joke': "Why don’t cricketers ever get sunburned? Because they have too many good covers!",
  'explanation': "The joke is a pun on 'covers' — in cricket it's a fielding position, but it also means protection from the sun."
}
```

---

✅ So, unlike your last version where you only saw the **explanation**, this setup gives you a **dictionary with both the joke and explanation**.


<img width="1291" height="711" alt="image" src="https://github.com/user-attachments/assets/790a153b-138d-4bb7-80ad-feabc5fbb927" />
