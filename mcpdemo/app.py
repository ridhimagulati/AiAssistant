import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient

async def main():
    # Load environment variables
    load_dotenv()

    # Ask user for a query
    user_query = input("Enter your question for the AI Assistant: ").strip()
    if not user_query:
        print("No input provided. Exiting.")
        return

    # MCP server configuration
    config = {
        "mcpServers": {
            "playwright": {
                "command": "npx",
                "args": ["@playwright/mcp@latest"],
                "env": {
                    "DISPLAY": ":1"
                }
            }
        }
    }

    # Initialize MCP client
    client = MCPClient.from_dict(config)

    # Set up OpenAI LLM
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0.7
    )

    # Create MCP Agent
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=30
    )

    # Run agent with user's query
    result = await agent.run(user_query)
    print(f"\nAI Assistant Response:\n{result}")

if __name__ == "__main__":
    asyncio.run(main())
