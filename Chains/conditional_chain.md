## **1. What are we doing here?**

We are teaching two AI friends:

* **Gemini** (from Google) → A good *classifier*, tells us if a review is **positive** or **negative**.
* **Gemma** (from HuggingFace) → A good *writer*, writes replies to customers.

Our mission:
When someone writes a restaurant review:

* If it’s **positive** → We say “Thanks! ❤️”
* If it’s **negative** → We say “Sorry! 😔”

---

## **2. Step-by-step like a child building Lego**

### Step 1 — Call our AI friends

```python
llm = HuggingFaceEndpoint(...)  # Connect to Gemma (writer)
model = ChatHuggingFace(llm=llm)

gemini_model = ChatGoogleGenerativeAI(...)  # Connect to Gemini (classifier)
```

We have 2 friends now.

---

### Step 2 — Tell Gemini how to answer

We make **rules** so Gemini *must* tell us `"positive"` or `"negative"` — nothing else.

```python
class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = ...
```

This is like saying:

> “Gemini, don’t draw dinosaurs, only say ‘positive’ or ‘negative’.”

---

### Step 3 — Make the “Classification Machine”

```python
prompt1 = PromptTemplate(
    template='Analyze the sentiment ... {feedback} ... {format_instructions}',
    ...
)
classifier_chain = prompt1 | gemini_model | parser2
```

This is a little **machine**:

1. Put in a review → Prompt tells Gemini “Check if it’s positive or negative.”
2. Gemini answers → Parser checks if it’s in correct format.

---

### Step 4 — Make two reply styles

* **For happy customers:**

```python
prompt2 = PromptTemplate(
    template='Write a grateful ...'
)
```

* **For unhappy customers:**

```python
prompt3 = PromptTemplate(
    template='Write an apologetic ...'
)
```

---

### Step 5 — Build the “Branch”

```python
branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)
```

Think of **RunnableBranch** like a “choose your own adventure” story:

* If review is **positive** → Go down the “thanks” path.
* If review is **negative** → Go down the “sorry” path.
* Else → Say “I’m confused.”

---

### Step 6 — Put the machines together

```python
chain = classifier_chain | branch_chain
```

* **First machine** → Figure out sentiment.
* **Second machine** → Choose the right response.

---

### Step 7 — Test it!

```python
print(chain.invoke({'feedback': 'The food was absolutely delicious ...'}))
```

Here:

1. Gemini → says `"positive"`.
2. Gemma → writes a **thank-you** note.

---

✅ **In short:**
Your code is:

1. **Classify** review → (Positive / Negative)
2. **Pick** the right style of reply
3. **Write** it using the correct AI



<img width="1427" height="613" alt="image" src="https://github.com/user-attachments/assets/6c87a016-b4eb-4003-b5dd-6339ae94c398" />


<img width="226" height="591" alt="image" src="https://github.com/user-attachments/assets/577d8f31-54a4-4f81-a395-1f68a585de66" />
