"""Tests for club-related tools."""

import pytest
from unittest.mock import patch, MagicMock
from transfermarkt_mcp.tools.clubs import search_clubs, get_club_profile, get_club_players


class TestSearchClubs:
    """Test cases for search_clubs function."""

    def test_search_clubs_empty_name(self):
        """Test search with empty club name."""
        result = search_clubs("")
        assert "error" in result
        assert "cannot be empty" in result["error"]

    def test_search_clubs_invalid_page(self):
        """Test search with invalid page number."""
        result = search_clubs("Bayern", page_number=0)
        assert "error" in result
        assert "must be positive" in result["error"]

    @patch('transfermarkt_mcp.client.client')
    def test_search_clubs_success(self, mock_client, sample_club_data):
        """Test successful club search."""
        mock_client.get.return_value = {"clubs": [sample_club_data]}

        result = search_clubs("Bayern", page_number=1)

        mock_client.get.assert_called_once_with(
            "clubs/search/Bayern",
            params={"page_number": 1}
        )
        assert "clubs" in result

    @patch('transfermarkt_mcp.client.client')
    def test_search_clubs_api_error(self, mock_client):
        """Test search with API error."""
        mock_client.get.return_value = {"error": "API unavailable"}

        result = search_clubs("Bayern")

        assert "error" in result
        assert result["error"] == "API unavailable"


class TestGetClubProfile:
    """Test cases for get_club_profile function."""

    def test_get_club_profile_empty_id(self):
        """Test getting profile with empty club ID."""
        result = get_club_profile("")
        assert "error" in result
        assert "cannot be empty" in result["error"]

    @patch('transfermarkt_mcp.client.client')
    def test_get_club_profile_success(self, mock_client, sample_club_data):
        """Test successful club profile retrieval."""
        mock_client.get.return_value = sample_club_data

        result = get_club_profile("27")

        mock_client.get.assert_called_once_with("clubs/27/profile")
        assert result == sample_club_data

    @patch('transfermarkt_mcp.client.client')
    def test_get_club_profile_not_found(self, mock_client):
        """Test club profile not found."""
        mock_client.get.return_value = {"error": "Club not found"}

        result = get_club_profile("999")

        assert "error" in result
        assert result["error"] == "Club not found"


class TestGetClubPlayers:
    """Test cases for get_club_players function."""

    def test_get_club_players_empty_id(self):
        """Test getting players with empty club ID."""
        result = get_club_players("")
        assert "error" in result
        assert "cannot be empty" in result["error"]

    @patch('transfermarkt_mcp.client.client')
    def test_get_club_players_success(self, mock_client, sample_players_data):
        """Test successful club players retrieval."""
        mock_client.get.return_value = sample_players_data

        result = get_club_players("27")

        mock_client.get.assert_called_once_with(
            "clubs/27/players",
            params={}
        )
        assert result == sample_players_data

    @patch('transfermarkt_mcp.client.client')
    def test_get_club_players_with_season(self, mock_client, sample_players_data):
        """Test club players retrieval with season filter."""
        mock_client.get.return_value = sample_players_data

        result = get_club_players("27", season_id="2023")

        mock_client.get.assert_called_once_with(
            "clubs/27/players",
            params={"season_id": "2023"}
        )
        assert result == sample_players_data

    @patch('transfermarkt_mcp.client.client')
    def test_get_club_players_no_players(self, mock_client):
        """Test club with no players."""
        mock_client.get.return_value = {"players": []}

        result = get_club_players("27")

        assert "players" in result
        assert result["players"] == []


# Integration-style tests with full client mock
class TestClubToolsIntegration:
    """Integration tests with full client behavior simulation."""

    @patch('transfermarkt_mcp.client.TransfermarktClient')
    def test_search_and_get_profile_flow(self, mock_client_class, sample_club_data):
        """Test typical user flow: search then get profile."""
        # Setup mock client instance
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client

        # Mock search response
        mock_client.get.side_effect = [
            {"clubs": [{"id": "27", "name": "Bayern Munich"}]},  # search result
            sample_club_data  # profile result
        ]

        # Test search
        with patch('transfermarkt_mcp.client.client', mock_client):
            search_result = search_clubs("Bayern")
            assert "clubs" in search_result

            # Test get profile using ID from search
            profile_result = get_club_profile("27")
            assert profile_result == sample_club_data

        # Verify calls
        assert mock_client.get.call_count == 2