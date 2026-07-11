from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers.structured import StructuredOutputParser, ResponseSchema
load_dotenv()

model = ChatOpenAI()
schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 fact about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)
"""
{'fact_1': 'Black holes are regions in space where gravity is so strong that nothing, not even light, can escape from them.', 
'fact_2': 'The boundary surrounding a black hole is called the event horizon. Once an object crosses the event horizon, it is impossible for it to escape the gravitational pull of the black hole.', 
'fact_3': 'Black holes can come in different sizes, with stellar black holes formed from the remains of massive stars and supermassive black holes found at the centers of galaxies, containing millions to billions of times the mass of our sun.'}"""