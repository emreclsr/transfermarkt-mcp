"""Tests for competition-related tools."""

import pytest
from unittest.mock import patch
from transfermarkt_mcp.tools.competitions import search_competitions, get_competition_clubs, get_competition_details


class TestSearchCompetitions:
    """Test cases for search_competitions function."""

    def test_search_competitions_empty_name(self):
        """Test search with empty competition name."""
        result = search_competitions("")
        assert "error" in result
        assert "cannot be empty" in result["error"]

    def test_search_competitions_invalid_page(self):
        """Test search with invalid page number."""
        result = search_competitions("Premier League", page_number=0)
        assert "error" in result
        assert "must be positive" in result["error"]

    @patch('transfermarkt_mcp.client.client')
    def test_search_competitions_success(self, mock_client, sample_competition_data):
        """Test successful competition search."""
        mock_client.get.return_value = {"competitions": [sample_competition_data]}

        result = search_competitions("Premier League", page_number=1)

        mock_client.get.assert_called_once_with(
            "competitions/search/Premier League",
            params={"page_number": 1}
        )
        assert "competitions" in result

    @patch('transfermarkt_mcp.client.client')
    def test_search_competitions_api_error(self, mock_client):
        """Test search with API error."""
        mock_client.get.return_value = {"error": "API unavailable"}

        result = search_competitions("Premier League")

        assert "error" in result
        assert result["error"] == "API unavailable"


class TestGetCompetitionClubs:
    """Test cases for get_competition_clubs function."""

    def test_get_competition_clubs_empty_id(self):
        """Test getting clubs with empty competition ID."""
        result = get_competition_clubs("")
        assert "error" in result
        assert "cannot be empty" in result["error"]

    @patch('transfermarkt_mcp.client.client')
    def test_get_competition_clubs_success(self, mock_client, sample_clubs_data):
        """Test successful competition clubs retrieval."""
        mock_client.get.return_value = sample_clubs_data

        result = get_competition_clubs("TR1")

        mock_client.get.assert_called_once_with("competitions/TR1/clubs")
        assert result == sample_clubs_data

    @patch('transfermarkt_mcp.client.client')
    def test_get_competition_clubs_not_found(self, mock_client):
        """Test competition clubs not found."""
        mock_client.get.return_value = {"error": "Competition not found"}

        result = get_competition_clubs("INVALID")

        assert "error" in result
        assert result["error"] == "Competition not found"


class TestGetCompetitionDetails:
    """Test cases for get_competition_details function."""

    def test_get_competition_details_empty_id(self):
        """Test getting details with empty competition ID."""
        result = get_competition_details("")
        assert "error" in result
        assert "cannot be empty" in result["error"]

    @patch('transfermarkt_mcp.client.client')
    def test_get_competition_details_success(self, mock_client, sample_competition_data):
        """Test successful competition details retrieval."""
        mock_client.get.return_value = sample_competition_data

        result = get_competition_details("TR1")

        mock_client.get.assert_called_once_with("competitions/TR1")
        assert result == sample_competition_data

    @patch('transfermarkt_mcp.client.client')
    def test_get_competition_details_not_found(self, mock_client):
        """Test competition details not found."""
        mock_client.get.return_value = {"error": "Competition not found"}

        result = get_competition_details("INVALID")

        assert "error" in result
        assert result["error"] == "Competition not found"
