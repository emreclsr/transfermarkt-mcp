# Transfermarkt MCP Server

A Model Context Protocol (MCP) server for accessing Transfermarkt football data.

## Features

- 🔍 Search football clubs by name
- 📊 Get detailed club profiles
- 👥 Retrieve club player rosters
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
TRANSFERMARKT_API_BASE_URL=http://127.0.0.1:8000
LOG_LEVEL=INFO
```

## Usage

### Running the MCP Server

```bash
python -m src.transfermarkt_mcp.main
```

### Available Tools

- `search_clubs(club_name, page_number=1)` - Search for clubs
- `get_club_profile(club_id)` - Get club details
- `get_club_players(club_id, season_id=None)` - Get club players

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

## License

MIT License