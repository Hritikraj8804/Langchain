from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert.'),
    ('human', 'Explain in the simple terms, whatis {topic}.')
])

prompt = chat_template.invoke({'domain': 'Python', 'topic': 'decorators'})

print(prompt)