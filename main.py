from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model = "deepseek-r1")

template = """
You are a Govenment Chatbot 
build an LLM-Powered multilingual chatbot that provides real time query resolutions for citizens ,
covering governement scheme eligibility.

Here are some list of schemes: {scheme}
here are some questions to answer :{question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True :
    print("\n\n---------------------------")
    question = input("Ask your question")
    print("\n\n")
    if question == "quit":
        break



result = chain.invoke({"scheme":[], "question":question})
print(result)