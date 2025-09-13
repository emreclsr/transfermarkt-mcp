"""Test configuration and fixtures."""

import pytest
from unittest.mock import Mock
from transfermarkt_mcp.client import TransfermarktClient


@pytest.fixture
def mock_client():
    """Mock Transfermarkt client for testing."""
    client = Mock(spec=TransfermarktClient)
    return client


@pytest.fixture
def sample_club_data():
    """Sample club data for testing."""
    return {
        "id": "27",
        "name": "Bayern Munich",
        "country": "Germany",
        "league": "Bundesliga",
        "market_value": "€825.00m"
    }


@pytest.fixture
def sample_players_data():
    """Sample players data for testing."""
    return {
        "players": [
            {
                "id": "8198",
                "name": "Robert Lewandowski",
                "position": "Centre-Forward",
                "market_value": "€45.00m"
            }
        ]
    }