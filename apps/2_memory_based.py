from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

history = []   #memory based chat history

while True:

    
    query = input("User: ")

    if query.lower() in ["exit", "quit"]:
        print("Goodbye...!")
        break

    history.append({"role": "user", "content": query})
    # print("User: ", query)

    res = llm.invoke(history)
    history.append({"role": "ai", "content" : res.text})
    print("AI: ", res.text)