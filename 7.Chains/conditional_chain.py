from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from langchain_core.output_parsers import StrOutputParser
from typing import Literal

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

class Feedback(BaseModel):

    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

# result = classifier_chain.invoke({'feedback':'this is a shit phone'})
# print(result) #sentiment='negative'

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feeedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negatve feedback \n {feedback}',
    input_variables=['feeedback']
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x:"Could not find sentiment")
)
chain = classifier_chain | branch_chain

result = chain.invoke({'feedback':'This is a product'})

print(result)
"""Positive- result = chain.invoke({'feedback':'This is a great product'})

Thank you so much for the kind words! I'm glad I was able to help and that you are satisfied with my service. Let me know if there is anything else I can assist you with in the future.

Negative- result = chain.invoke({'feedback':'This is a bad product'})

I'm sorry to hear that you had a negative experience. Can you please provide more details so that we can address your concerns and make things right? Your feedback is important to us.
Grey- result = chain.invoke({'feedback':'This is a product'})

hank you for sharing your feedback with us. We apologize for any inconvenience or frustration you may have experienced. We will take your comments into consideration and use them to improve our services in the future. If there is anything specific you would like to discuss further, please do not hesitate to reach out to us.
"""
