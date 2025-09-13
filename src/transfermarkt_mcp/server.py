"""MCP server setup and tool registration."""

import logging
from fastmcp import FastMCP

logger = logging.getLogger(__name__)


def create_mcp_server() -> FastMCP:
    """Create and configure the MCP server instance with all tools."""
    mcp = FastMCP(
        name="Transfermarkt MCP Server",
        dependencies=["requests", "python-dotenv"],
    )

    # Import tools to register them
    from transfermarkt_mcp.tools.clubs import register_club_tools

    register_club_tools(mcp)

    return mcp
