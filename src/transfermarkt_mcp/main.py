"""Main entry point for the Transfermarkt MCP server."""

import logging
from transfermarkt_mcp.server import create_mcp_server

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the MCP server instance at module level for fastmcp run
mcp = create_mcp_server()


def main() -> None:
    """Run the MCP server."""
    try:
        logger.info("Starting Transfermarkt MCP Server...")
        mcp.run()
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server error: {e}")
        raise


if __name__ == "__main__":
    main()
