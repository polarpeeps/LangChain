from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables  import RunnableParallel, RunnableSequence, RunnablePassthrough

load_dotenv()
prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)
parser = StrOutputParser()
model = ChatOpenAI()
prompt2 = PromptTemplate(
    template="Explain the following joke \n {joke}",
    input_variables=['joke']
)
joke_gen_chain = RunnableSequence(prompt1,model,parser)
parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2,model,parser)
})

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)

result = final_chain.invoke({'topic':'FIFA'})
print(result)
"""
{'joke': 'Why did the FIFA player go to the doctor? Because he had too many penalties!', 'explanation': 'This joke is based on a play on words. In the context of FIFA (the popular video game series based on soccer), penalties are a type of foul that can result in a player being penalized by the referee. In this joke, it is suggesting that the FIFA player went to the doctor because he had too many penalties in the game, meaning he was performing poorly and making mistakes, so he needed to seek help or advice from a professional.'}
"""