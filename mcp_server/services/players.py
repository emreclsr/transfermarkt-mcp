import requests
from typing import Optional
from mcp_server.config.settings import mcp, BASE_URL


@mcp.tool
def search_players(player_name: str, page_number: int = 1):
    """Search for players by name with pagination support."""
    try:
        response = requests.get(f"{BASE_URL}/players/search/{player_name}", params={"page_number": page_number})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to search players: {str(e)}"}

@mcp.tool
def get_player_by_id(player_id: int):
    """Get detailed information about a specific player."""
    try:
        response = requests.get(f"{BASE_URL}/players/{player_id}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to get player details: {str(e)}"}


@mcp.tool
def get_player_profile(player_id: int):
    """Get detailed profile information for a player."""
    try:
        response = requests.get(f"{BASE_URL}/players/{player_id}/profile")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to get player profile: {str(e)}"}



@mcp.tool
def get_player_market_value(player_id: int):
    """Get market value information for a specific player."""
    try:
        response = requests.get(f"{BASE_URL}/players/{player_id}/market_value")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to get player market value: {str(e)}"}

@mcp.tool
def get_player_transfers(player_id: int):
    """Get transfer history of a player."""
    try:
        response = requests.get(f"{BASE_URL}/players/{player_id}/transfers")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to get player transfers: {str(e)}"}

@mcp.tool
def get_player_jersey_numbers(player_id: int):
    """Get jersey numbers history for a player."""
    try:
        response = requests.get(f"{BASE_URL}/players/{player_id}/jersey_numbers")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to get player jersey numbers: {str(e)}"}

@mcp.tool
def get_player_stats(player_id: int, season: Optional[int] = None):
    """Get player statistics with optional season filter."""
    try:
        params = {"season": season} if season else None
        response = requests.get(f"{BASE_URL}/players/{player_id}/stats", params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to get player stats: {str(e)}"}


@mcp.tool
def get_player_injuries(player_id: int):
    """Get injury history for a player."""
    try:
        response = requests.get(f"{BASE_URL}/players/{player_id}/injuries")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to get player injuries: {str(e)}"}

@mcp.tool
def get_player_achievements(player_id: int):
    """Get achievements and trophies for a player."""
    try:
        response = requests.get(f"{BASE_URL}/players/{player_id}/achievements")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to get player achievements: {str(e)}"}



