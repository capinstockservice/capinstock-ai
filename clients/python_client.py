"""Пример: вызов инструментов CapinStock из Python с личным ключом.

pip install "mcp>=2"
CAPINSTOCK_TOKEN=csk_... python python_client.py
"""
import asyncio
import os

from mcp import Client
from mcp.client.streamable_http import streamable_http_client
from mcp.shared._httpx_utils import create_mcp_http_client


async def main() -> None:
    token = os.environ["CAPINSTOCK_TOKEN"]
    http = create_mcp_http_client(headers={"Authorization": f"Bearer {token}"})
    async with Client(streamable_http_client("https://mcp.capinstock.com/mcp", http_client=http)) as client:
        tools = await client.list_tools()
        print("Доступные инструменты:", ", ".join(t.name for t in tools.tools))
        result = await client.call_tool("get_purchase_recommendations", {"horizon_days": 14})
        print(result.content[0].text)


asyncio.run(main())
