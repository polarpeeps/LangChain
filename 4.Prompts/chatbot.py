from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
chat_history = []
while True:
    user_input = input("You: ")
    if str.lower(user_input) =="exit":
        break
    chat_history.append(user_input)

    result = model.invoke(chat_history)
    chat_history.append(result.content)

    print("ChatGpt: ", result.content)

print(chat_history)
"CHAT HISTORY NEED--"
"""
You: WHICH NUMBER IS GREATER 69 OR 67
ChatGpt:  69
You: MULTIPLY THE GREATER ONE WITH 10
ChatGpt:  The result depends on the two numbers being multiplied. Can you please provide the two numbers so that I can help you calculate the result?
You: I GAVE YOU TWO NUMBERS BEFORE
ChatGpt:  I apologize for the oversight. Could you please provide me with the numbers again so that I can assist you further?
You: DO YOU NOT REMEMBER          
ChatGpt:  I'm sorry, I do not have the ability to remember past interactions or conversations. I am programmed to provide information and assistance to the best of my ability in each new interaction.
You: EXIT
"""

"SOLUTION TEMP-"
"""
You: 
ChatGpt:  Hello! How can I assist you today?
You: WHICH NUMBER IS GREATER 69 OR 67
ChatGpt:  69 is greater than 67.
You: MULTIPLY THE GREATER ONE WITH 10
ChatGpt:  69 x 10 = 690
You: exit
['', 'Hello! How can I assist you today?', 'WHICH NUMBER IS GREATER 69 OR 67', '69 is greater than 67.', 'MULTIPLY THE GREATER ONE WITH 10', '69 x 10 = 690']
"""