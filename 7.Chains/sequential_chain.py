from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic': 'Unemployment in India'})

print(result)

chain.get_graph().print_ascii()

"""
1. The unemployment rate in India reached an all-time high of 23.5% in April 2020 but has since decreased to around 7-8%.
2. Lack of job creation in key sectors such as agriculture and manufacturing is a major factor contributing to unemployment in India.
3. High population growth and a mismatch between skills and job requirements due to the education system are also contributing factors.
4. The informal sector, which lacks regular employment opportunities and benefits, contributes to underemployment and low wages in India.
5. Government programs like MGNREGA have been implemented to address unemployment but critics argue they have not created sustainable job opportunities on a large scale.
     +-------------+       
     | PromptInput |       
     +-------------+       
            *
            *
            *
    +----------------+
    | PromptTemplate |
    +----------------+
            *
            *
            *
      +------------+
      | ChatOpenAI |
      +------------+
            *
            *
            *
   +-----------------+
   | StrOutputParser |
   +-----------------+
            *
            *
            *
+-----------------------+
| StrOutputParserOutput |
+-----------------------+
            *
            *
            *
    +----------------+
    | PromptTemplate |
    +----------------+
            *
            *
            *
      +------------+
      | ChatOpenAI |
      +------------+
            *
            *
            *
   +-----------------+
   | StrOutputParser |
   +-----------------+
            *
            *
            *
+-----------------------+
| StrOutputParserOutput |
"""