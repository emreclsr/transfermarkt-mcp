import logging

logger = logging.getLogger(__name__)


def search_competitions(competition_name: str, page_number: int = 1):
    """
    Search for competitions by name with pagination support.

    Args:
        competition_name (str): Name of the competition to search for
        page_number (int): Page number for pagination (default: 1)

    Returns:
        dict: Dictionary containing search results or error information
    """
    from transfermarkt_mcp.client import client

    if not competition_name.strip():
        return {"error": "Competition name cannot be empty"}

    if page_number < 1:
        return {"error": "Page number must be positive"}

    logging.info(
        f"Searching for competitions: '{competition_name}', page: {page_number}"
    )

    return client.get(
        f"competitions/search/{competition_name}", params={"page_number": page_number}
    )


def get_competition_clubs(competition_id: str):
    """Get all clubs participating in a specific competition.

    Args:
        competition_id (str): The competition ID (e.g. 'TR1' for Turkish Super Lig)

    Returns:
        dict: Dictionary containing clubs data or error information
    """
    from transfermarkt_mcp.client import client

    if not competition_id.strip():
        return {"error": "Competition ID cannot be empty"}

    logging.info(f"Getting clubs for competition ID: {competition_id}")

    return client.get(f"competitions/{competition_id}/clubs")


def get_competition_details(competition_id: str):
    """Get detailed information about a specific competition.

    Args:
        competition_id (str): The competition ID (e.g. 'TR1' for Turkish Super Lig)

    Returns:
        dict: Dictionary containing competition details or error information
    """
    from transfermarkt_mcp.client import client

    if not competition_id.strip():
        return {"error": "Competition ID cannot be empty"}

    logging.info(f"Getting competition details for ID: {competition_id}")

    return client.get(f"competitions/{competition_id}")


def register_competition_tools(mcp) -> None:
    """Register all club tools with the MCP server."""
    # Use the decorator syntax that FastMCP expects
    mcp.tool()(search_competitions)
    mcp.tool()(get_competition_clubs)
    mcp.tool()(get_competition_details)

    logger.info(
        "Registered competition tools: search_competitions, get_competition_clubs, get_competition_details"
    )
