"""Club-related MCP tools."""

import logging
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)


def search_clubs(club_name: str, page_number: int = 1) -> Dict[str, Any]:
    """
    Search for clubs by name with pagination support.

    Args:
        club_name: Name of the club to search for
        page_number: Page number for pagination (default: 1)

    Returns:
        Dictionary containing search results or error information
    """
    from transfermarkt_mcp.client import client

    if not club_name.strip():
        return {"error": "Club name cannot be empty"}

    if page_number < 1:
        return {"error": "Page number must be positive"}

    logger.info(f"Searching for clubs: '{club_name}', page: {page_number}")

    return client.get(f"clubs/search/{club_name}", params={"page_number": page_number})


def get_club_profile(club_id: str) -> Dict[str, Any]:
    """
    Get detailed profile information for a specific club.

    Args:
        club_id: Unique identifier of the club

    Returns:
        Dictionary containing club profile data or error information
    """
    from transfermarkt_mcp.client import client

    if not club_id.strip():
        return {"error": "Club ID cannot be empty"}

    logger.info(f"Getting club profile for ID: {club_id}")

    return client.get(f"clubs/{club_id}/profile")


def get_club_players(club_id: str, season_id: Optional[str] = None) -> Dict[str, Any]:
    """
    Get players list for a specific club, optionally filtered by season.

    Args:
        club_id: Unique identifier of the club
        season_id: Optional season identifier for filtering

    Returns:
        Dictionary containing players data or error information
    """
    from transfermarkt_mcp.client import client

    if not club_id.strip():
        return {"error": "Club ID cannot be empty"}

    logger.info(
        f"Getting players for club ID: {club_id}, season: {season_id or 'current'}"
    )

    params = {}
    if season_id:
        params["season_id"] = season_id

    return client.get(f"clubs/{club_id}/players", params=params)


def register_club_tools(mcp) -> None:
    """Register all club tools with the MCP server."""
    # Use the decorator syntax that FastMCP expects
    mcp.tool()(search_clubs)
    mcp.tool()(get_club_profile)
    mcp.tool()(get_club_players)

    logger.info(
        "Registered club tools: search_clubs, get_club_profile, get_club_players"
    )
