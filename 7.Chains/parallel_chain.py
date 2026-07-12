from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatOpenAI()
model2 = ChatOpenAI() # use claude this is just for example

prompt1 = PromptTemplate(
    template='Generate short and simplle noted from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate a 5 short quiz question answers  from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided Notes and Quiz into a single document \n Notes-> {notes} \n \n Quiz-> \n {quiz}',
    input_variables=['notes','quiz']
)

parser = StrOutputParser()
text = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
"""

parallel = RunnableParallel({
    'notes':prompt1 | model1 | parser,
    'quiz' : prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser
chain = parallel | merge_chain

result = chain.invoke({'text':text})

print(result)
chain.get_graph().print_ascii()


"""
Notes:
- SVMs are used for classification, regression, and outliers detection.
- Advantages include effectiveness in high dimensional spaces and memory efficiency.
- Support vectors are used in the decision function.
- Different Kernel functions can be specified.
- Disadvantages include the risk of over-fitting if the number of features is much greater than samples.
- SVMs do not directly provide probability estimates.
- Support both dense and sparse sample vectors as input.
- For optimal performance, use C-ordered numpy.ndarray or scipy.sparse.csr_matrix with dtype=float64.

Quiz:
1. What are support vector machines used for?
- Classification, regression, and outliers detection

2. What is a key advantage of support vector machines?
- Effective in high dimensional spaces

3. What is a disadvantage of support vector machines?
- Do not directly provide probability estimates

4. What are the subset of training points used in the decision function called?
- Support vectors

5. How does support vector machines handle memory efficiency?
- Uses a subset of training points in the decision function
            +---------------------------+
            | Parallel<notes,quiz>Input |
            +---------------------------+
                 **               **
              ***                   ***
            **                         **
+----------------+                +----------------+
| PromptTemplate |                | PromptTemplate |
+----------------+                +----------------+
          *                               *
          *                               *
          *                               *
  +------------+                    +------------+
  | ChatOpenAI |                    | ChatOpenAI |
  +------------+                    +------------+
          *                               *
          *                               *
          *                               *
+-----------------+              +-----------------+
| StrOutputParser |              | StrOutputParser |
+-----------------+              +-----------------+
                 **               **
                   ***         ***
                      **     **
           +----------------------------+
           | Parallel<notes,quiz>Output |
           +----------------------------+
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