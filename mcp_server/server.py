from mcp_server.config.settings import mcp
# Import all service modules to register tools
from mcp_server.services import club
from mcp_server.services import players
from mcp_server.services import competitions

if __name__ == "__main__":
    mcp.run()