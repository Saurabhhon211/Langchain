from dotenv import load_dotenv
load_dotenv()
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch


llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash")
tools = [TavilySearch()]
agent = create_agent(model=llm,tools=tools)

if __name__ == "__main__":
    while True:
        query = input("Enter your query: ")
        response = agent.invoke({"messages": [{"role": "user", "content": query}]})
        print(f"Response: {response['messages'][-1].text}")