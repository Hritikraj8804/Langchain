
## **Step-by-step explanation**

### **1. Load tools**

```python
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
```

* **PromptTemplate** → Holds your question format.
* **HuggingFaceEndpoint** → Connects to the AI model (Gemma).
* **StrOutputParser** → Makes sure AI output is clean text.

---

### **2. Create the prompt**

```python
prompt = PromptTemplate(
    template='genernate 5 name from {country}',
    input_variables=['country']
)
```

This is the **instruction** to the AI.
If you pass `country="korea"`, it becomes:

```
genernate 5 name from korea
```

*(typo “genernate” doesn’t break it, but you might want “generate”)*

---

### **3. Connect to HuggingFace model**

```python
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)
```

* Using **Gemma 2B** from Google via HuggingFace for text generation.

---

### **4. Add a parser**

```python
parser = StrOutputParser()
```

* Turns AI output into plain string (no extra formatting).

---

### **5. Make the chain**

```python
chain = prompt | model | parser
```

The pipeline works like:

1. **Prompt** → Fill in the `{country}`.
2. **Model** → AI writes 5 names.
3. **Parser** → Output cleaned up.

---

### **6. Run it**

```python
result = chain.invoke({'country': 'korea'})
```

* Pass `"korea"` to the prompt.
* AI might return something like:

```
1. Ji-hoon  
2. Min-seo  
3. Hye-jin  
4. Dong-hyun  
5. Soo-jin
```

---

### **7. Show the chain structure**

```python
chain.get_graph().print_ascii()
```

You’ll see a simple **linear pipeline** like:

```
PromptTemplate -> ChatHuggingFace -> StrOutputParser
```

---




<img width="1172" height="348" alt="Screenshot 2025-08-14 234339" src="https://github.com/user-attachments/assets/dd9756f6-2b86-4d87-b21d-270dce94a3da" />


<img width="497" height="767" alt="image" src="https://github.com/user-attachments/assets/8e1626ea-097d-4c3c-9469-5cf0bf633ccb" />
