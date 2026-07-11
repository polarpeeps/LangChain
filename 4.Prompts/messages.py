from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()
messages=[
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about LangChain")
]

result = model.invoke(messages)
messages.append(AIMessage(result.content))

print(messages)
"""[SystemMessage(content='You are a helpful assistant', additional_kwargs={}, response_metadata={}),
 HumanMessage(content='Tell me about LangChain', additional_kwargs={}, response_metadata={}),
 AIMessage(content="I'm not sure about a specific company or platform called LangChain. Can you provide more information or context so I can assist you better?", 
 additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[])]"""