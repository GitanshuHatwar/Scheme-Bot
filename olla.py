import ollama 

client = ollama.Client()

model = "deepseek-r1"
prompt = "Gross collection and net collection of the Stranger Stings Season 1,2,3"

response = client.generate(model = model , prompt = prompt )

print(response.response)