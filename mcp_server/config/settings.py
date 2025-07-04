import os

from fastmcp import FastMCP

mcp = FastMCP(
    name="Transfermarkt Clubs API",
    dependencies=["requests"],
)

# Change this to your actual API URL
BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000")