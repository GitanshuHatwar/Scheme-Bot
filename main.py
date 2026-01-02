from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever 
model = OllamaLLM(model = "deepseek-r1")

template = """
You are a Government Chatbot 
build an LLM-Powered multilingual chatbot that provides real time query resolutions for citizens ,
covering government scheme eligibility.

Here are some list of schemes: {scheme}
here are some questions to answer :{question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True :
    print("\n\n---------------------------")
    question = input("Ask your question: ")
    print("\n\n")
    if question.lower() == "quit":
        break

    # Retrieve relevant schemes based on the question
    docs = retriever.invoke(question)
    
    # Extract page content from the documents for a cleaner prompt
    context = "\n".join([doc.page_content for doc in docs])
    
    # Run the chain with the retrieved schemes and the user question
    result = chain.invoke({"scheme": context, "question": question})
    print(result)
