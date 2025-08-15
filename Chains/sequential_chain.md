
## **Step-by-step explanation**

### **1. Load your tools**

```python
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
```

* **PromptTemplate** → Makes structured instructions for the AI.
* **StrOutputParser** → Turns AI’s response into plain text.
* **HuggingFaceEndpoint** → Connects to HuggingFace model (here: Gemma).

---

### **2. Create prompts**

```python
prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)
```

* Job 1 → AI writes a **long, detailed report** on the topic.

```python
prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)
```

* Job 2 → AI takes a big chunk of text and makes **5 bullet points**.

---

### **3. Connect to HuggingFace model**

```python
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)
```

* **Gemma 2B** is your “writer” and “summarizer”.

---

### **4. Build the chain**

```python
chain = prompt1 | model | parser | prompt2 | model | parser
```

This is a **pipeline**:

1. **prompt1** → Make the “detailed report”.
2. **model** → Gemma writes it.
3. **parser** → Convert AI text to plain text.
4. **prompt2** → Take that report and ask for 5 points.
5. **model** → Gemma summarizes.
6. **parser** → Get plain text again.

---

### **5. Run it**

```python
result = chain.invoke({'topic': 'korean culture'})
```

* First, Gemma writes a **detailed report on Korean culture**.
* Then, Gemma reads her own writing and gives **5 bullet points**.

---

### **6. Visualize it**

```python
chain.get_graph().print_ascii()
```

This prints something like:

```
   Prompt1 -> Model -> Parser -> Prompt2 -> Model -> Parser
```

A straight **flow of tasks**, no branches.

---

💡 This is a **sequential chain** (everything happens one after another), not parallel.

---





<img width="1575" height="875" alt="image" src="https://github.com/user-attachments/assets/7ae11571-c8f0-4abd-900d-c0047b8b3f31" />
