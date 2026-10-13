from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_community.utilities import GoogleSerperAPIWrapper
from langgraph.checkpoint.memory import MemorySaver

model = ChatGroq(model="openai/gpt-oss-20b")
search = GoogleSerperAPIWrapper()
memory = MemorySaver()
#thread_config = {"configurable": {"thread_id": "1"}}

agent = create_agent(
    model = model,
    tools = [search.run],
    checkpointer= memory,
    system_prompt="You are a agent and can search for any question on google."
)

while True:

    query = input("User: ")

    if query.lower() in ["quiet", "exit"]:
        print("GoodBye...")
        break

   # response = agent.invoke({"message":[{"role":"user", "content": query}]})

    response = agent.invoke({
        "messages": [("user", query)]},
        {"configurable": {"thread_id": "asd1234"}}
    )

    print("AI:", response["messages"][-1].content)































#--------------------------------------------------------------------------------


# from dotenv import load_dotenv
# load_dotenv()

# from langchain_groq import ChatGroq
# from langchain.agents import create_agent
# from langchain_google_community import GoogleSerperAPIWrapper
# from langchain_core.tools import Tool

# # 1. Initialize the LLM
# model = ChatGroq(model="openai/gpt-oss-20b")

# # 2. Initialize Google Search
# search = GoogleSerperAPIWrapper()

# # 3. Convert the search function into a LangChain tool
# search_tool = Tool(
#     name="GoogleSearch",
#     func=search.run,
#     description="Search Google for current information about a topic."
# )

# # 4. Create the AI agent
# agent = create_agent(
#     model=model,
#     tools=[search_tool],
#     system_prompt=(
#         "You are a helpful AI agent. "
#         "Use Google Search when you need current information. "
#         "Answer clearly and accurately."
#     )
# )

# # 5. Chat loop
# while True:
#     query = input("User: ").strip()

#     if query.lower() in ["quit", "exit"]:
#         print("Goodbye!")
#         break

#     try:
#         response = agent.invoke({
#             "messages": [
#                 {"role": "user", "content": query}
#             ]
#         })

#         print("AI:", response["messages"][-1].content)

#     except Exception as e:
#         print("Error:", e)
