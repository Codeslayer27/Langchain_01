from dotenv import load_dotenv
#from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain.schema import AIMessage, HumanMessage, SystemMessage

load_dotenv()

model = ChatGroq(model_name = "llama-3.3-70b-versatile"
)

chat_history = []

SystemMessage = SystemMessage(content="You are a helpful AI assistant.")
chat_history.append(SystemMessage)

while True:
    query = input("You: ")
    if query.lower()=="exit":
        break
    chat_history.append(HumanMessage(content=query))

    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))

    print(f"AI:{response}")

print("-----Message History----")
print(chat_history)
    
