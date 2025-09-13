"""Tests for player-related tools."""

import pytest
from unittest.mock import patch
from transfermarkt_mcp.tools.players import (
    search_players, get_player_by_id, get_player_profile, get_player_market_value,
    get_player_transfers, get_player_jersey_numbers, get_player_stats,
    get_player_injuries, get_player_achievements
)


class TestSearchPlayers:
    """Test cases for search_players function."""

    def test_search_players_empty_name(self):
        """Test search with empty player name."""
        result = search_players("")
        assert "error" in result
        assert "cannot be empty" in result["error"]

    def test_search_players_invalid_page(self):
        """Test search with invalid page number."""
        result = search_players("Messi", page_number=0)
        assert "error" in result
        assert "must be positive" in result["error"]

    @patch('transfermarkt_mcp.client.client')
    def test_search_players_success(self, mock_client, sample_player_data):
        """Test successful player search."""
        mock_client.get.return_value = {"players": [sample_player_data]}

        result = search_players("Messi", page_number=1)

        mock_client.get.assert_called_once_with(
            "players/search/Messi",
            params={"page_number": 1}
        )
        assert "players" in result

    @patch('transfermarkt_mcp.client.client')
    def test_search_players_api_error(self, mock_client):
        """Test search with API error."""
        mock_client.get.return_value = {"error": "API unavailable"}

        result = search_players("Messi")

        assert "error" in result
        assert result["error"] == "API unavailable"


class TestGetPlayerById:
    """Test cases for get_player_by_id function."""

    def test_get_player_by_id_empty_id(self):
        """Test getting player with empty ID."""
        result = get_player_by_id("")
        assert "error" in result
        assert "cannot be empty" in result["error"]

    @patch('transfermarkt_mcp.client.client')
    def test_get_player_by_id_success(self, mock_client, sample_player_data):
        """Test successful player retrieval by ID."""
        mock_client.get.return_value = sample_player_data

        result = get_player_by_id("8198")

        mock_client.get.assert_called_once_with("players/8198")
        assert result == sample_player_data

    @patch('transfermarkt_mcp.client.client')
    def test_get_player_by_id_not_found(self, mock_client):
        """Test player not found."""
        mock_client.get.return_value = {"error": "Player not found"}

        result = get_player_by_id("999999")

        assert "error" in result
        assert result["error"] == "Player not found"


class TestGetPlayerProfile:
    """Test cases for get_player_profile function."""

    def test_get_player_profile_empty_id(self):
        """Test getting profile with empty player ID."""
        result = get_player_profile("")
        assert "error" in result
        assert "cannot be empty" in result["error"]

    @patch('transfermarkt_mcp.client.client')
    def test_get_player_profile_success(self, mock_client, sample_player_data):
        """Test successful player profile retrieval."""
        mock_client.get.return_value = sample_player_data

        result = get_player_profile("8198")

        mock_client.get.assert_called_once_with("players/8198/profile")
        assert result == sample_player_data


class TestGetPlayerMarketValue:
    """Test cases for get_player_market_value function."""

    def test_get_player_market_value_empty_id(self):
        """Test getting market value with empty player ID."""
        result = get_player_market_value("")
        assert "error" in result
        assert "cannot be empty" in result["error"]

    @patch('transfermarkt_mcp.client.client')
    def test_get_player_market_value_success(self, mock_client):
        """Test successful player market value retrieval."""
        market_value_data = {"market_value": "€45.00m", "history": []}
        mock_client.get.return_value = market_value_data

        result = get_player_market_value("8198")

        mock_client.get.assert_called_once_with("players/8198/market_value")
        assert result == market_value_data


class TestGetPlayerTransfers:
    """Test cases for get_player_transfers function."""

    def test_get_player_transfers_empty_id(self):
        """Test getting transfers with empty player ID."""
        result = get_player_transfers("")
        assert "error" in result
        assert "cannot be empty" in result["error"]

    @patch('transfermarkt_mcp.client.client')
    def test_get_player_transfers_success(self, mock_client):
        """Test successful player transfers retrieval."""
        transfers_data = {"transfers": []}
        mock_client.get.return_value = transfers_data

        result = get_player_transfers("8198")

        mock_client.get.assert_called_once_with("players/8198/transfers")
        assert result == transfers_data


class TestGetPlayerJerseyNumbers:
    """Test cases for get_player_jersey_numbers function."""

    def test_get_player_jersey_numbers_empty_id(self):
        """Test getting jersey numbers with empty player ID."""
        result = get_player_jersey_numbers("")
        assert "error" in result
        assert "cannot be empty" in result["error"]

    @patch('transfermarkt_mcp.client.client')
    def test_get_player_jersey_numbers_success(self, mock_client):
        """Test successful player jersey numbers retrieval."""
        jersey_data = {"jersey_numbers": []}
        mock_client.get.return_value = jersey_data

        result = get_player_jersey_numbers("8198")

        mock_client.get.assert_called_once_with("players/8198/jersey_numbers")
        assert result == jersey_data


class TestGetPlayerStats:
    """Test cases for get_player_stats function."""

    def test_get_player_stats_empty_id(self):
        """Test getting stats with empty player ID."""
        result = get_player_stats("")
        assert "error" in result
        assert "cannot be empty" in result["error"]

    @patch('transfermarkt_mcp.client.client')
    def test_get_player_stats_success(self, mock_client):
        """Test successful player stats retrieval."""
        stats_data = {"stats": []}
        mock_client.get.return_value = stats_data

        result = get_player_stats("8198")

        mock_client.get.assert_called_once_with("players/8198/stats", params={})
        assert result == stats_data

    @patch('transfermarkt_mcp.client.client')
    def test_get_player_stats_with_season(self, mock_client):
        """Test player stats retrieval with season filter."""
        stats_data = {"stats": []}
        mock_client.get.return_value = stats_data

        result = get_player_stats("8198", season="2023")

        mock_client.get.assert_called_once_with("players/8198/stats", params={"season": "2023"})
        assert result == stats_data


class TestGetPlayerInjuries:
    """Test cases for get_player_injuries function."""

    def test_get_player_injuries_empty_id(self):
        """Test getting injuries with empty player ID."""
        result = get_player_injuries("")
        assert "error" in result
        assert "cannot be empty" in result["error"]

    @patch('transfermarkt_mcp.client.client')
    def test_get_player_injuries_success(self, mock_client):
        """Test successful player injuries retrieval."""
        injuries_data = {"injuries": []}
        mock_client.get.return_value = injuries_data

        result = get_player_injuries("8198")

        mock_client.get.assert_called_once_with("players/8198/injuries")
        assert result == injuries_data


class TestGetPlayerAchievements:
    """Test cases for get_player_achievements function."""

    def test_get_player_achievements_empty_id(self):
        """Test getting achievements with empty player ID."""
        result = get_player_achievements("")
        assert "error" in result
        assert "cannot be empty" in result["error"]

    @patch('transfermarkt_mcp.client.client')
    def test_get_player_achievements_success(self, mock_client):
        """Test successful player achievements retrieval."""
        achievements_data = {"achievements": []}
        mock_client.get.return_value = achievements_data

        result = get_player_achievements("8198")

        mock_client.get.assert_called_once_with("players/8198/achievements")
        assert result == achievements_data
