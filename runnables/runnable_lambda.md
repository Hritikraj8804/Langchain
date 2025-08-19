
### 🔎 Step-by-step breakdown


```python
def word_count(text):
    return len(text.split())
```

Helper function to count words in a given string.

---

```python
prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)
```

Creates a template that expects an input variable `topic`.
Example input: `{'topic': 'AI'}` → Prompt: `"Write a joke about AI"`

---

```python
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash"
)
```

Sets up the Gemini model.

---

```python
parser = StrOutputParser()
```

Parses the model’s response into a plain string (instead of a full object).

---

```python
joke_gen_chain = RunnableSequence(prompt, model, parser)
```

This is a **chain**:

1. Takes `{topic}`
2. Formats prompt (`"Write a joke about AI"`)
3. Sends to Gemini
4. Parses into plain joke text

✅ Output: `"Some joke string"`

---

```python
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_count)
})
```

Here’s the **problem** ⚠️:

* `RunnablePassthrough()` → just passes the input dictionary forward without changing it.
  So instead of the **joke text**, you’ll still get `{'topic': 'AI'}`.

* `RunnableLambda(word_count)` → tries to call `word_count` on that same input.
  But your `word_count` expects a string, not a dict → so it breaks.

---

```python
final_chain = RunnableSequence(joke_gen_chain, parallel_chain)
```

This means:

1. Generate a joke string from `joke_gen_chain`.
2. Pass that joke string into `parallel_chain`.

BUT inside `parallel_chain`, `RunnablePassthrough` is just echoing the joke string correctly, while `RunnableLambda(word_count)` works only if the input is **already a string**.

Since you chained it correctly (`RunnableSequence(joke_gen_chain, parallel_chain)`), the input to `parallel_chain` **is the joke string** — so actually your current code should **work**.

Example flow:

```
{'topic':'AI'} 
   → joke_gen_chain → "AI joke string" 
   → parallel_chain → { 'joke': "AI joke string", 'word_count': 12 }
```

✅ That’s why it prints properly.

---

### 🛠 Why the confusion?

Your original **intention** (based on how you wrote `RunnablePassthrough`) might have been that the joke string comes directly from `joke_gen_chain`.
And yes, because you wrapped them in `RunnableSequence`, the input to `parallel_chain` is already the joke text, so `RunnablePassthrough()` works fine here.

But if you **didn’t** wrap them in sequence, you’d need to replace `RunnablePassthrough()` with `joke_gen_chain`.

---

### ✅ Simplified mental model

Think of it like a factory pipeline:

1. **Prompt → Model → Parser** = produces **joke string**
2. **Parallel** =

   * Just return the string (`RunnablePassthrough`)
   * Run word count on it (`RunnableLambda`)
3. Merge results → `{ 'joke': "...", 'word_count': N }`

---



<img width="855" height="50" alt="image" src="https://github.com/user-attachments/assets/e949eb40-a927-4def-9b78-d10c8f685458" />
