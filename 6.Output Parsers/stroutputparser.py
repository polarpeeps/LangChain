from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="google/gemma-2-2b-it",
#     task="text-generation"
# )

model = ChatOpenAI()

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

prompt1 = template1.invoke({'topic':'black hole'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result.content})

result1 = model.invoke(prompt2)

print(result1.content)
"""
Black holes are regions in space where gravity is so strong that nothing, not even light, can escape from them.
They are formed when massive stars collapse at the end of their life cycle, creating a singularity with infinite density and zero volume. 
There are three main types of black holes: stellar, supermassive, and intermediate. Black holes are characterized by properties like the event horizon, singularity, accretion disk, and jets of high-speed particles. Despite advancements in understanding, 
black holes remain mysterious and continue to fascinate scientists and enthusiasts with their extreme forces and enigmatic nature.
"""