from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
repo_id="meta-llama/Llama-3.1-8B-Instruct",task="text-generation"
)

chat = ChatHuggingFace(llm=llm)

response = chat.invoke("Who has 8 Ballon Dors?")

print(response.content)