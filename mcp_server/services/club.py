import requests

from typing import Optional

from mcp_server.config.settings import mcp, BASE_URL


@mcp.tool
def search_clubs(club_name: str, page_number: int = 1):
    """Search for clubs by name with pagination support."""
    try:
        response = requests.get(f"{BASE_URL}/clubs/search/{club_name}", params={"page_number": page_number})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to search clubs: {str(e)}"}


@mcp.tool
def get_club_profile(club_id: str):
    """Get detailed profile information for a specific club."""
    try:
        response = requests.get(f"{BASE_URL}/clubs/{club_id}/profile")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to get club profile: {str(e)}"}


@mcp.tool
def get_club_players(club_id: str, season_id: Optional[str] = None):
    """Get players list for a specific club, optionally filtered by season."""
    try:
        params = {}
        if season_id:
            params["season_id"] = season_id

        response = requests.get(f"{BASE_URL}/clubs/{club_id}/players", params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to get club players: {str(e)}"}