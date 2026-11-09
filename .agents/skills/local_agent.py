import asyncio
from agent_framework import Agent
from agent_framework.foundry import FoundryLocalClient

async def main():
    agent = Agent(
        client=FoundryLocalClient(model="qwen2.5-0.5b"),
        name="LocalAgent",
        instructions="You are a helpful local assistant.",
    )
    result = await agent.run("Bonjour, qui es-tu ?")
    print(result)

asyncio.run(main())