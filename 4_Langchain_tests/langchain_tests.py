from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

template = """
Pytanie: {question}
Rozumuj krok po kroku.
Odpowiedź:
"""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm = ChatOpenAI(model_name="gpt-4o")
llm_chain = LLMChain(prompt=prompt, llm=llm)

question = """
Jakie są najważniejsze aspekty związane ze sztuczną inteligencją?
"""

response = llm_chain.run(question)
print(response)
