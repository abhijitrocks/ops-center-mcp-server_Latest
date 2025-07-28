from mcp.server.fastmcp import FastMCP
from opscenter import resources, tools, prompts, storage

# Initialize with your Google Sheets ID
storage.init("1O4uFUtRqATIRx29IAyaJMtkR1oMTBiiAxPkCZmKnZ_o")

mcp = FastMCP(
    name="OPS Center MCP",
    json_response=True,
)

resources.register(mcp)
tools.register(mcp)
prompts.register(mcp)

if __name__ == "__main__":
    mcp.run(transport="stdio")
