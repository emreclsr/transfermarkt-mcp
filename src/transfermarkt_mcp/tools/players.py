"""Player-related MCP tools."""

import logging
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)


def search_players(player_name: str, page_number: int = 1) -> Dict[str, Any]:
    """
    Search for players by name with pagination support.

    Args:
        player_name: Name of the player to search for
        page_number: Page number for pagination (default: 1)

    Returns:
        Dictionary containing search results or error information
    """
    from transfermarkt_mcp.client import client

    if not player_name.strip():
        return {"error": "Player name cannot be empty"}

    if page_number < 1:
        return {"error": "Page number must be positive"}

    logger.info(f"Searching for players: '{player_name}', page: {page_number}")

    return client.get(
        f"players/search/{player_name}", params={"page_number": page_number}
    )


def get_player_by_id(player_id: str) -> Dict[str, Any]:
    """
    Get detailed information about a specific player.

    Args:
        player_id: Unique identifier of the player

    Returns:
        Dictionary containing player data or error information
    """
    from transfermarkt_mcp.client import client

    if not player_id.strip():
        return {"error": "Player ID cannot be empty"}

    logger.info(f"Getting player details for ID: {player_id}")

    return client.get(f"players/{player_id}")


def get_player_profile(player_id: str) -> Dict[str, Any]:
    """
    Get detailed profile information for a player.

    Args:
        player_id: Unique identifier of the player

    Returns:
        Dictionary containing player profile data or error information
    """
    from transfermarkt_mcp.client import client

    if not player_id.strip():
        return {"error": "Player ID cannot be empty"}

    logger.info(f"Getting player profile for ID: {player_id}")

    return client.get(f"players/{player_id}/profile")


def get_player_market_value(player_id: str) -> Dict[str, Any]:
    """
    Get market value information for a specific player.

    Args:
        player_id: Unique identifier of the player

    Returns:
        Dictionary containing market value data or error information
    """
    from transfermarkt_mcp.client import client

    if not player_id.strip():
        return {"error": "Player ID cannot be empty"}

    logger.info(f"Getting market value for player ID: {player_id}")

    return client.get(f"players/{player_id}/market_value")


def get_player_transfers(player_id: str) -> Dict[str, Any]:
    """
    Get transfer history of a player.

    Args:
        player_id: Unique identifier of the player

    Returns:
        Dictionary containing transfer history or error information
    """
    from transfermarkt_mcp.client import client

    if not player_id.strip():
        return {"error": "Player ID cannot be empty"}

    logger.info(f"Getting transfer history for player ID: {player_id}")

    return client.get(f"players/{player_id}/transfers")


def get_player_jersey_numbers(player_id: str) -> Dict[str, Any]:
    """
    Get jersey numbers history for a player.

    Args:
        player_id: Unique identifier of the player

    Returns:
        Dictionary containing jersey numbers history or error information
    """
    from transfermarkt_mcp.client import client

    if not player_id.strip():
        return {"error": "Player ID cannot be empty"}

    logger.info(f"Getting jersey numbers for player ID: {player_id}")

    return client.get(f"players/{player_id}/jersey_numbers")


def get_player_stats(player_id: str, season: Optional[str] = None) -> Dict[str, Any]:
    """
    Get player statistics with optional season filter.

    Args:
        player_id: Unique identifier of the player
        season: Optional season identifier for filtering

    Returns:
        Dictionary containing player statistics or error information
    """
    from transfermarkt_mcp.client import client

    if not player_id.strip():
        return {"error": "Player ID cannot be empty"}

    logger.info(
        f"Getting stats for player ID: {player_id}, season: {season or 'current'}"
    )

    params = {}
    if season:
        params["season"] = season

    return client.get(f"players/{player_id}/stats", params=params)


def get_player_injuries(player_id: str) -> Dict[str, Any]:
    """
    Get injury history for a player.

    Args:
        player_id: Unique identifier of the player

    Returns:
        Dictionary containing injury history or error information
    """
    from transfermarkt_mcp.client import client

    if not player_id.strip():
        return {"error": "Player ID cannot be empty"}

    logger.info(f"Getting injury history for player ID: {player_id}")

    return client.get(f"players/{player_id}/injuries")


def get_player_achievements(player_id: str) -> Dict[str, Any]:
    """
    Get achievements and trophies for a player.

    Args:
        player_id: Unique identifier of the player

    Returns:
        Dictionary containing achievements data or error information
    """
    from transfermarkt_mcp.client import client

    if not player_id.strip():
        return {"error": "Player ID cannot be empty"}

    logger.info(f"Getting achievements for player ID: {player_id}")

    return client.get(f"players/{player_id}/achievements")


def register_player_tools(mcp) -> None:
    """Register all player tools with the MCP server."""
    # Use the decorator syntax that FastMCP expects
    mcp.tool()(search_players)
    mcp.tool()(get_player_by_id)
    mcp.tool()(get_player_profile)
    mcp.tool()(get_player_market_value)
    mcp.tool()(get_player_transfers)
    mcp.tool()(get_player_jersey_numbers)
    mcp.tool()(get_player_stats)
    mcp.tool()(get_player_injuries)
    mcp.tool()(get_player_achievements)

    logger.info(
        "Registered player tools: search_players, get_player_by_id, get_player_profile, "
        "get_player_market_value, get_player_transfers, get_player_jersey_numbers, "
        "get_player_stats, get_player_injuries, get_player_achievements"
    )
