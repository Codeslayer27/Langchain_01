from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv() #this loads up my OPENAI_API_KEY from .env file

model = ChatOpenAI(model="gpt-4o")

result = model.invoke("What is 81 divided by 9?")
print("Full result:")
print(result)
print(result.content)