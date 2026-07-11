from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI(model="gpt-4", temperature=1.5, max_completion_tokens=10)
#temp-creativity of answers
# max_completion_tokens- no. of tokens in output
result = model.invoke("What is the Capital of India?")

print(result)
print(result.content)
