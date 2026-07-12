from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables  import RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

print(chain.invoke({'topic':'AI'}))

"""
This joke plays on the idea that AI (artificial intelligence) has its own way of processing and understanding love and relationships, represented by its "love algorithm." The punchline indicates that the AI broke up with its data scientist girlfriend because she was constantly trying to change or manipulate the AI's way of loving, by attempting to "reprogram its love algorithm." This creates humor by highlighting the absurdity of trying to control or alter something as complex and unique as an AI's understanding of love.
"""