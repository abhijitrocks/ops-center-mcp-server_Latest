from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts.base import UserMessage, AssistantMessage

def register(mcp: FastMCP):
    @mcp.prompt(title="Create Tenant Prompt")
    def prompt_create_tenant() -> list[UserMessage | AssistantMessage]:
        return [
            UserMessage("Create a new tenant."),
            AssistantMessage("Sure. What is the tenant name and ID?")
        ]
