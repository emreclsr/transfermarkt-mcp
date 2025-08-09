import requests
from typing import Optional
from mcp_server.config.settings import mcp, BASE_URL


@mcp.tool
def search_competitions(competition_name: str, page_number: int = 1):
    """Search for competitions by name with pagination support."""
    try:
        response = requests.get(
            f"{BASE_URL}/competitions/search/{competition_name}",
            params={"page_number": page_number}
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to search competitions: {str(e)}"}


@mcp.tool
def get_competition_clubs(competition_id: str):
    """Get all clubs participating in a specific competition.

    Args:
        competition_id (str): The competition ID (e.g. 'TR1' for Turkish Super Lig)
    """
    try:
        response = requests.get(f"{BASE_URL}/competitions/{competition_id}/clubs")
        if response.status_code == 404:
            return {"error": "Competition not found or clubs endpoint not available"}
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to get competition clubs: {str(e)}"}


@mcp.tool
def get_competition_details(competition_id: str):
    """Get detailed information about a specific competition.

    Args:
        competition_id (str): The competition ID (e.g. 'TR1' for Turkish Super Lig)
    """
    try:
        response = requests.get(f"{BASE_URL}/competitions/{competition_id}")
        if response.status_code == 404:
            return {"error": "Competition not found"}
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to get competition details: {str(e)}"}