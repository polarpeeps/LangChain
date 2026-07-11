from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

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
parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({'topic':'FC Barcelona'})

print(result)

"""FC Barcelona, founded in 1899, is a successful and popular football club based in Barcelona, Spain. They play at the Camp Nou, the largest stadium in Europe, wearing blue and red jerseys. Their possession-based style of play, 'tiki-taka', has led to numerous domestic and international trophies. The club's renowned youth academy, La Masia, has developed world-class players like Messi and Iniesta. Barcelona's fierce rivalry with Real Madrid, commitment to social causes, and dedication to youth development showcase their influence in the football world."""