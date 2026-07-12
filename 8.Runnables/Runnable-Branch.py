from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables  import RunnableBranch, RunnableSequence,RunnableLambda,RunnablePassthrough

load_dotenv()

prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
)

model = ChatOpenAI()

parser = StrOutputParser()

report_gen_chain = prompt1 | model | parser

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>300, prompt2 | model | parser),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

print(final_chain.invoke({'topic':'Russia vs Ukraine'}))
'''
The conflict between Russia and Ukraine has a long history stemming from the collapse of the Soviet Union in 1991. The most recent conflict began in 2014 with Russia's annexation of Crimea, leading to a separatist movement in eastern Ukraine. The international community has condemned Russia's actions, leading to tensions between Russia and the West. Despite attempts at diplomacy, the conflict remains unresolved and has resulted in widespread violence, destruction, and a humanitarian crisis in Ukraine. Finding a resolution will require difficult compromises and a commitment to peaceful dialogue.
'''