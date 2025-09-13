# Transfermarkt MCP Server

A Model Context Protocol (MCP) server for accessing Transfermarkt football data.

## Features

- 🔍 Search football clubs by name
- 📊 Get detailed club profiles
- 👥 Retrieve club player rosters
- 🏆 Search and get competition information
- ⚽ Search for individual players
- 📄 Pagination support for search results
- 🔧 Season-based filtering for players

## Installation

1. Clone the repository:
```bash
git clone https://github.com/emreclsr/transfermarkt-mcp.git
cd transfermarkt-mcp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```
or
```bash
poetry install
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API configuration
```

## Configuration

Create a `.env` file with:
```
TRANSFERMARKT_API_BASE_URL=https://transfermarkt-api.fly.dev
LOG_LEVEL=INFO
```

## Usage

### Running the MCP Server

```bash
python -m src.transfermarkt_mcp.main
```

### Available Tools

#### Club Tools
- `search_clubs(club_name, page_number=1)` - Search for clubs
- `get_club_profile(club_id)` - Get club details
- `get_club_players(club_id, season_id=None)` - Get club players

#### Competition Tools
- `search_competitions(competition_name, page_number=1)` - Search for competitions by name
- `get_competition_clubs(competition_id)` - Get all clubs participating in a specific competition

#### Player Tools
- `search_players(player_name, page_number=1)` - Search for players by name
- `get_player_by_id(player_id)` - Get detailed information about a specific player

## Development

### Running Tests
```bash
pytest tests/
```

### Code Quality
```bash
black src/
flake8 src/
```

## Claude Desktop Config Example
```json
{
  "mcpServers": {
    "transfermarkt": {
      "command": "your-uv-location/uv",
      "args": [
        "run",
        "--with",
        "fastmcp",
        "--with",
        "requests",
        "fastmcp",
        "run",
        "your-workdir/transfermarkt-mcp/src/transfermarkt_mcp/main.py"
      ],
      "cwd": "your-workdir/transfermarkt-mcp/src",
      "env": {
        "BASE_URL": "https://transfermarkt-api.fly.dev",
        "PYTHONPATH": "your-workdir/transfermarkt-mcp/src"
      }
    }
  }
}
```


## License

MIT License
