"""Command-line application demonstrating Schwab API usage."""

import argparse
import json
from schwab_app.schwab_client import SchwabClient


def main() -> None:
    parser = argparse.ArgumentParser(description="Schwab API demo")
    parser.add_argument("api_key", help="Schwab API key")
    parser.add_argument("access_token", help="OAuth access token")
    parser.add_argument("symbol", help="Symbol to query")
    parser.add_argument("account_id", help="Account ID")
    args = parser.parse_args()

    client = SchwabClient(api_key=args.api_key, access_token=args.access_token)

    print("Fetching account information...")
    accounts = client.get_accounts()
    print(json.dumps(accounts, indent=2))

    print("\nFetching positions...")
    positions = client.get_positions(args.account_id)
    print(json.dumps(positions, indent=2))

    print("\nFetching quote...")
    quote = client.get_quote(args.symbol)
    print(json.dumps(quote, indent=2))

    print("\nSearching instruments...")
    search = client.search_instruments(args.symbol)
    print(json.dumps(search, indent=2))

    print("\nFetching news...")
    news = client.get_news(args.symbol)
    print(json.dumps(news, indent=2))

    print("\nFetching historical prices...")
    hist = client.get_historical_prices(args.symbol)
    print(json.dumps(hist, indent=2))


if __name__ == "__main__":
    main()
