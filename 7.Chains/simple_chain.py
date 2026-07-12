from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic:football'})

print(result)

chain.get_graph().print_ascii()

"""
1. The modern game of football (soccer) originated in England in the 19th century, with the official rules being codified in 1863 by the newly formed Football Association.

2. The FIFA World Cup is the most widely viewed and followed football tournament in the world, with an estimated 3.5 billion viewers tuning in to watch the 2018 edition.

3. The longest professional football game on record lasted 219 minutes and took place in 2017 in Norway. The match eventually ended in a 4-2 victory after 8 rounds of penalty shootouts.

4. The fastest goal scored in a professional football match was by Nawaf Al Abed of Saudi Arabia, who scored just two seconds into a game in 2009.

5. The highest-scoring football match in history took place in Madagascar in 2002, with AS Adema defeating Stade Olympique L'Emyrne 149-0. All 149 goals were scored by AS Adema players deliberately scoring own goals in protest against a refereeing decision in a previous match.
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
"""