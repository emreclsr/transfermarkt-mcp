"""Configuration management for the MCP server."""

import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration constants
DEFAULT_BASE_URL = "http://127.0.0.1:8000"
DEFAULT_TIMEOUT = 30
DEFAULT_LOG_LEVEL = "INFO"

logger = logging.getLogger(__name__)


class Config:
    """Application configuration."""

    def __init__(self) -> None:
        self.base_url = os.getenv("TRANSFERMARKT_API_BASE_URL", DEFAULT_BASE_URL)
        self.request_timeout = int(os.getenv("REQUEST_TIMEOUT", DEFAULT_TIMEOUT))
        self.log_level = os.getenv("LOG_LEVEL", DEFAULT_LOG_LEVEL)

        # Configure logging
        logging.getLogger().setLevel(getattr(logging, self.log_level.upper()))

        logger.info(
            f"Config loaded: base_url={self.base_url}, timeout={self.request_timeout}"
        )


# Global config instance
config = Config()
