from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables  import RunnableParallel, RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a twitter post about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a linkedin post about {topic}',
    input_variables=['topic']
)

parser= StrOutputParser()
model = ChatOpenAI()
parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1,model, parser),
    'linkedin': RunnableSequence(prompt2,model, parser),
}
)

result  = parallel_chain.invoke({'topic':'FIFA'})

print(result)
result = {'tweet': '"Just watched the latest FIFA match and the intensity was unreal! The skill and talent on display never fail to amaze me. #FIFA #soccer #sports"', 
          'linkedin': "Exciting news for all FIFA fans! The highly anticipated FIFA 22 has finally been released and it's bigger and better than ever. With updated player ratings, improved gameplay mechanics, and new features like the HyperMotion technology, this game is sure to take your gaming experience to the next level. Whether you're a casual player or a competitive gamer, FIFA 22 has something for everyone. Who's ready to hit the pitch and show off their skills? #FIFA22 #gaming #soccer #EASports"}