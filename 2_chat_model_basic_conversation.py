from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    temperature=0,
    model_name = "llama-3.3-70b-versatile"
)

messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?")
]

"""
result = model.invoke(messages)
print(f"Answer from AI: {result.content}")
"""

#with AIMEssage
messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
    AIMessage(content="81 divided by 9 is 9"),
    HumanMessage(content="What is 5 multiplyed by 10?")
]

result = model.invoke(messages)
print(f"Answer from AI: {result.content}")

