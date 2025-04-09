import os
import asyncio
from dotenv import load_dotenv
from browser_use.agent.service import Agent
from browser_use.controller.service import Controller
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API Key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Set up LLM and Controller
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", google_api_key=api_key)
controller = Controller()

# Define user story (now called task_description)
task_description = """
Go to https://www.google.com,
search for 'Playwright Python',
click the first result,
confirm the page title contains 'Playwright'.
"""

async def main():
    # Use correct keyword: task_description
    agent = Agent(task_description, llm=llm, controller=controller, use_vision=False)
    history = await agent.run()
    
    print("\n--- Execution Logs ---")
    for action in history.action_results():
        print(action)

    print("\n--- Final Result ---")
    print(history.final_result())

if __name__ == "__main__":
    asyncio.run(main())
