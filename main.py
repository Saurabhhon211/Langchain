from dotenv import load_dotenv
load_dotenv()
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from tavily import TavilyClient



tavily = TavilyClient()
@tool
def search(query):
    """Search the web for current information."""
    print(f"Searching for ::{query}")
    return tavily.search(query=query)

llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash")
tools = [search]
agent = create_agent(model=llm,tools=tools)

if __name__ == "__main__":
    while True:
        query = input("Enter your query: ")
        response = agent.invoke({"messages": [{"role": "user", "content": query}]})
        print(f"Response: {response['messages'][-1].text}")