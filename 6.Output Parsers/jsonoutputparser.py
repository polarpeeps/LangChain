from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatOpenAI()
parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)
"""{'fact1': 'Black holes are formed when a massive star collapses under its own gravity.', 'fact2': 'Black holes have such strong gravity that not even light can escape from them, making them invisible to the naked eye.', 'fact3': 'Black holes can vary in size, with some being as small as a single atom and others being as large as millions of times the mass of our sun.', 'fact4': 'Black holes distort time and space around them, creating a region known as the event horizon where the laws of physics as we know them break down.', 'fact5': 'Despite their fearsome reputation, black holes are not necessarily destructive and can play a key role in the formation of galaxies and other celestial bodies.'}"""