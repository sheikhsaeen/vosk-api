import os
from typing import Dict, Any, Optional
import requests

class SchwabClient:
    """Simple client for the Charles Schwab Developer API."""

    def __init__(self, api_key: str, access_token: Optional[str] = None):
        self.api_key = api_key
        self.access_token = access_token or os.getenv("SCHWAB_ACCESS_TOKEN")
        self.base_url = "https://api.schwab.com"

    def _headers(self) -> Dict[str, str]:
        if not self.access_token:
            raise ValueError("Access token required")
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "schwab-api-key": self.api_key,
        }

    def get_accounts(self) -> Dict[str, Any]:
        """Retrieve account information."""
        url = f"{self.base_url}/accounts"
        response = requests.get(url, headers=self._headers())
        response.raise_for_status()
        return response.json()

    def get_positions(self, account_id: str) -> Dict[str, Any]:
        """Retrieve positions for an account."""
        url = f"{self.base_url}/accounts/{account_id}/positions"
        response = requests.get(url, headers=self._headers())
        response.raise_for_status()
        return response.json()

    def get_quote(self, symbol: str) -> Dict[str, Any]:
        """Get a real-time quote for a symbol."""
        url = f"{self.base_url}/marketdata/{symbol}/quotes"
        response = requests.get(url, headers=self._headers())
        response.raise_for_status()
        return response.json()

    def search_instruments(self, query: str) -> Dict[str, Any]:
        """Search for instruments by symbol or name."""
        url = f"{self.base_url}/instruments"
        params = {"search": query}
        response = requests.get(url, headers=self._headers(), params=params)
        response.raise_for_status()
        return response.json()

    def place_order(self, account_id: str, order_data: Dict[str, Any]) -> Dict[str, Any]:
        """Place a trade order."""
        url = f"{self.base_url}/accounts/{account_id}/orders"
        response = requests.post(url, headers=self._headers(), json=order_data)
        response.raise_for_status()
        return response.json()

    def cancel_order(self, account_id: str, order_id: str) -> None:
        """Cancel an existing order."""
        url = f"{self.base_url}/accounts/{account_id}/orders/{order_id}"
        response = requests.delete(url, headers=self._headers())
        response.raise_for_status()

    def get_news(self, symbol: str) -> Dict[str, Any]:
        """Retrieve news articles for a given symbol."""
        url = f"{self.base_url}/marketdata/{symbol}/news"
        response = requests.get(url, headers=self._headers())
        response.raise_for_status()
        return response.json()

    def get_historical_prices(self, symbol: str, period: str = "1y") -> Dict[str, Any]:
        """Fetch historical price data."""
        url = f"{self.base_url}/marketdata/{symbol}/pricehistory"
        params = {"period": period}
        response = requests.get(url, headers=self._headers(), params=params)
        response.raise_for_status()
        return response.json()
