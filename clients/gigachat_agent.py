"""Пример: агент на GigaChat (GigaChain / LangGraph), который работает с CapinStock через MCP.

pip install langchain-mcp-adapters langchain-gigachat langgraph
GIGACHAT_CREDENTIALS=... CAPINSTOCK_TOKEN=csk_... python gigachat_agent.py
"""
import asyncio
import os

from langchain_gigachat.chat_models import GigaChat
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent


async def main() -> None:
    client = MultiServerMCPClient({
        "capinstock": {
            "transport": "streamable_http",
            "url": "https://mcp.capinstock.com/mcp",
            "headers": {"Authorization": f"Bearer {os.environ['CAPINSTOCK_TOKEN']}"},
        }
    })
    tools = await client.get_tools()
    model = GigaChat(credentials=os.environ["GIGACHAT_CREDENTIALS"], verify_ssl_certs=False)
    agent = create_react_agent(model, tools)
    answer = await agent.ainvoke({"messages": [("user", "Что мне заказать у поставщиков в ближайшие две недели?")]})
    print(answer["messages"][-1].content)


asyncio.run(main())
