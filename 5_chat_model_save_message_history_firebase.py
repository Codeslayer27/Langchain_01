from dotenv import load_dotenv
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_groq import ChatGroq
import os

load_dotenv()
#https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment
#getting from .env file
PROJECT_ID = os.getenv('PROJECT_ID')
SESSION_ID = os.getenv('SESSION_ID')
COLLECTION_NAME = os.getenv('COLLECTION_NAME')


print("Initializing Firestore client...")
client = firestore.Client(project=PROJECT_ID)

print("Initializing firestore char message history.")
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection = COLLECTION_NAME,
    client= client,
)

print("chat history initialized.")
print("current chat history:", chat_history.messages)

model = model = ChatGroq(model_name = "llama-3.3-70b-versatile"
)
print("Start chatting with AI type 'exit' to quit.")

while True:
    human_input = input("Users: ")
    if human_input.lower() =="exit":
        break
    chat_history.add_user_message(human_input)
    ai_response = model.invoke(chat_history.messages)
    chat_history.add_ai_message(ai_response.content)
    print(f"AI: {ai_response.content}")