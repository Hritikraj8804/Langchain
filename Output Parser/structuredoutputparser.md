
## 🔹 Step 1: Define a Schema

```python
schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]
```

* A **`ResponseSchema`** tells the model how we want the output to be structured.
* Here, we want **3 facts** about a topic, so we define:

  * `fact_1` → First fact
  * `fact_2` → Second fact
  * `fact_3` → Third fact

---

## 🔹 Step 2: Create a Parser

```python
parser = StructuredOutputParser.from_response_schemas(schema)
```

* This parser will enforce that the model’s output **follows the schema**.
* For example, it ensures the output looks like JSON with keys `"fact_1"`, `"fact_2"`, `"fact_3"`.

---

## 🔹 Step 3: Define the Prompt

```python
template = PromptTemplate(
    template='Give 3 fact about {topic} \n {format_instructions}',
    input_variables=['topic'],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)
```

* `{topic}` → placeholder for what subject we want facts about.
* `{format_instructions}` → automatically inserted instructions from the parser, telling the LLM **how to format the output** (usually JSON).

👉 Example final prompt when `topic="black hole"`:

```
Give 3 fact about black hole
Format your response as a JSON object with keys:
- fact_1: Fact 1 about the topic
- fact_2: Fact 2 about the topic
- fact_3: Fact 3 about the topic
```

---

## 🔹 Step 4: Create the Chain

```python
chain = template | model | parser
```

* `template` → fills in the prompt
* `model` → runs the LLM
* `parser` → parses the output into a **Python dictionary**

---

## 🔹 Step 5: Run the Chain

```python
result = chain.invoke({'topic':'black hole'})
print(result)
```

* Input: `{"topic": "black hole"}`
* Model generates structured JSON (facts).
* Parser converts it into a Python dict.

✅ Example Output:

```python
{
  'fact_1': 'A black hole has such strong gravity that not even light can escape.',
  'fact_2': 'They are formed from the collapse of massive stars.',
  'fact_3': 'Black holes can grow by absorbing nearby matter and merging with other black holes.'
}
```

---

### 🔑 In Short:

This code ensures that instead of random text, the LLM always gives **well-structured output** (facts inside a dict) that’s easy to use in your program. 🚀

---



<img width="1190" height="152" alt="image" src="https://github.com/user-attachments/assets/d04f951a-80f7-419e-bb1b-aabe1972edec" />
