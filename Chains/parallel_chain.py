from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model1 = ChatHuggingFace(llm=llm)

model2 = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """
Korean, Chinese, and Japanese are three major East Asian languages with distinct characteristics and writing systems.

Korean Language:
Korean uses the Hangul writing system, which is phonetic and consists of 24 basic letters. It is the official language of South Korea and North Korea, spoken by approximately 77 million people worldwide. Korean grammar follows a Subject-Object-Verb (SOV) word order and has complex honorific systems that reflect social relationships.

Chinese Language:
Chinese is the most spoken language in the world with over 1.3 billion speakers. It uses Chinese characters (hanzi) as its writing system, which are logographic. Mandarin Chinese is the official language of China and Taiwan. Chinese is a tonal language with four main tones in Mandarin, and grammar follows a Subject-Verb-Object (SVO) structure.

Japanese Language:
Japanese uses three writing systems: Hiragana, Katakana, and Kanji (borrowed Chinese characters). It is spoken by about 125 million people, primarily in Japan. Japanese grammar follows SOV word order and has complex levels of politeness and formality. The language has no grammatical gender or plural forms for most nouns.

Common features among these languages include the influence of Chinese characters in their writing systems and similar cultural concepts reflected in their vocabulary and expressions.
"""

result = chain.invoke({'text':text})

print(result)

