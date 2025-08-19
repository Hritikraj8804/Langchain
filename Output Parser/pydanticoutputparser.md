
### 1. **Model Setup**

```python
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
```

* You are using **Hugging Face Inference API** with the model `google/gemma-2-2b-it` (a fine-tuned instruction model).
* `HuggingFaceEndpoint` connects to Hugging Face Hub and provides text-generation.
* `ChatHuggingFace` wraps it so it works in LangChain’s `Runnable` pipeline.

---

### 2. **Defining a Pydantic Schema**

```python
class Person(BaseModel):
    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description='Name of the city the person belongs to')
```

* You create a **Pydantic model** called `Person` with fields:

  * `name` (string)
  * `age` (integer, must be >18)
  * `city` (string)

This schema tells the parser how to validate and structure the LLM output.

---

### 3. **Pydantic Output Parser**

```python
parser = PydanticOutputParser(pydantic_object=Person)
```

* `PydanticOutputParser` ensures the LLM’s response is **converted into a valid `Person` object**.
* It also provides **format instructions** (JSON schema-like structure) that are automatically injected into the prompt to guide the model’s output.

---

### 4. **Prompt Template**

```python
template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
```

* You ask the model: *“Generate the name, age and city of a fictional {place} person”*
* `{place}` will be replaced dynamically (e.g., `"korea"`).
* `{format_instruction}` inserts **parser instructions**, so the LLM outputs structured data (valid JSON).

---

### 5. **Chain Creation**

```python
chain = template | model | parser
```

* This pipeline:

  1. Formats the prompt.
  2. Sends it to the Hugging Face model.
  3. Parses the response into a `Person` object.

---

### 6. **Execution**

```python
final_result = chain.invoke({'place':'korea'})
print(final_result)
```

* Input: `"korea"`
* Model generates something like:

  ```json
  {
    "name": "Jihoon Park",
    "age": 27,
    "city": "Seoul"
  }
  ```
* Parser converts it into a `Person` instance:

  ```python
  Person(name="Jihoon Park", age=27, city="Seoul")
  ```

---

✅ **Final Output** (example):

```python
name='Jihoon Park' age=27 city='Seoul'
```

---



<img width="1080" height="63" alt="image" src="https://github.com/user-attachments/assets/a8ffdc02-0735-490c-b3c0-3f7bc82349f6" />
