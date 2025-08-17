"""HTTP client for Transfermarkt API interactions."""

import requests
import logging
from typing import Dict, Any, Optional
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from transfermarkt_mcp.config import config

logger = logging.getLogger(__name__)


class TransfermarktClient:
    """
    HTTP client for Transfermarkt API with retry logic
    and error handling.
    """

    def __init__(self) -> None:
        self.base_url = config.base_url.rstrip("/")
        self.timeout = config.request_timeout
        self.session = self._create_session()

    def _create_session(self) -> requests.Session:
        """Create a requests session with retry strategy."""
        session = requests.Session()

        # Configure retry strategy
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)

        return session

    def _make_request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Make an HTTP request with error handling."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        try:
            logger.debug(f"Making {method} request to {url}")
            response = self.session.request(
                method=method, url=url, timeout=self.timeout, **kwargs
            )
            response.raise_for_status()
            return response.json()

        except requests.exceptions.Timeout:
            return {"error": f"Request timed out after {self.timeout} seconds"}
        except requests.exceptions.ConnectionError:
            return {"error": "Failed to connect to the API"}
        except requests.exceptions.HTTPError as e:
            return {
                "error": f"HTTP error {e.response.status_code}: {e.response.reason}"
            }
        except requests.exceptions.RequestException as e:
            return {"error": f"Request failed: {str(e)}"}
        except ValueError as e:
            return {"error": f"Invalid JSON response: {str(e)}"}

    def get(
        self, endpoint: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Make a GET request."""
        return self._make_request("GET", endpoint, params=params)

    def close(self) -> None:
        """Close the HTTP session."""
        self.session.close()


# Global client instance
client = TransfermarktClient()
