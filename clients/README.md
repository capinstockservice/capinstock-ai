# Настройки для ИИ-клиентов

Везде адрес коннектора `https://mcp.capinstock.com/mcp`. Клиенты с входом через браузер (OAuth)
подключаются без ключа: при первом обращении откроется страница CapinStock «Разрешить доступ».
Там, где нужен ключ, создайте **личный ключ** в кабинете: раздел «ИИ-ассистенты». Ключ храните
как пароль и не публикуйте в репозиториях — используйте переменную окружения `CAPINSTOCK_TOKEN`.

## Cursor

`~/.cursor/mcp.json` (для всех проектов) или `.cursor/mcp.json` (для одного):

```json
{
  "mcpServers": {
    "capinstock": { "url": "https://mcp.capinstock.com/mcp" }
  }
}
```

С личным ключом:

```json
{
  "mcpServers": {
    "capinstock": {
      "url": "https://mcp.capinstock.com/mcp",
      "headers": { "Authorization": "Bearer ${env:CAPINSTOCK_TOKEN}" }
    }
  }
}
```

## VS Code + GitHub Copilot

`.vscode/mcp.json`:

```json
{
  "servers": {
    "capinstock": { "type": "http", "url": "https://mcp.capinstock.com/mcp" }
  }
}
```

С личным ключом (VS Code спросит его при первом запуске):

```json
{
  "inputs": [
    { "type": "promptString", "id": "capinstock-token", "description": "Личный ключ CapinStock", "password": true }
  ],
  "servers": {
    "capinstock": {
      "type": "http",
      "url": "https://mcp.capinstock.com/mcp",
      "headers": { "Authorization": "Bearer ${input:capinstock-token}" }
    }
  }
}
```

## Claude Code — проект с личным ключом

`.mcp.json` в корне проекта:

```json
{
  "mcpServers": {
    "capinstock": {
      "type": "http",
      "url": "https://mcp.capinstock.com/mcp",
      "headers": { "Authorization": "Bearer ${CAPINSTOCK_TOKEN}" }
    }
  }
}
```

## Codex — с личным ключом

`~/.codex/config.toml`:

```toml
[mcp_servers.capinstock]
url = "https://mcp.capinstock.com/mcp"
bearer_token_env_var = "CAPINSTOCK_TOKEN"
```

## Gemini CLI

```bash
gemini mcp add --transport http capinstock https://mcp.capinstock.com/mcp
```

## Devin Desktop (бывший Windsurf)

```bash
devin mcp add capinstock https://mcp.capinstock.com/mcp
devin mcp login capinstock
```

## n8n

Узел **MCP Client Tool** (инструмент для AI Agent) или **MCP Client** (шаг процесса):
транспорт HTTP Streamable, адрес `https://mcp.capinstock.com/mcp`, авторизация Bearer — личный ключ.

## Yandex AI Studio

**Agent Atelier → MCP servers → Create MCP server → External MCP server**: адрес
`https://mcp.capinstock.com/mcp`, транспорт Streamable HTTP, авторизация «Токен доступа» — личный ключ.
Затем подключите сервер к агенту.

## GigaChat — свой агент на GigaChain

Пример — [`gigachat_agent.py`](gigachat_agent.py).

## Microsoft Copilot Studio

**Tools → Add a tool → Model Context Protocol**: адрес `https://mcp.capinstock.com/mcp`, авторизация
**API key** (заголовок `Authorization`, значение `Bearer <ключ>`).

## OpenAI Responses API и другие SDK

Передавайте личный ключ как токен доступа: в OpenAI Responses API — поле `authorization` у
инструмента `type: "mcp"`, в Python SDK MCP — заголовок `Authorization`. Пример на Python —
[`python_client.py`](python_client.py).
