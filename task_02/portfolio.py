

import csv
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
TICKER_FILE = BASE_DIR / "market_prices.csv"
PRICE_FILE = BASE_DIR / "current_prices.csv"
OUTPUT_FILE = BASE_DIR / "portfolio_summary.csv"


def load_tickers():
    """Return ticker -> company name from the supplied ticker directory."""
    tickers = {}
    if TICKER_FILE.exists():
        with TICKER_FILE.open("r", newline="", encoding="utf-8-sig") as file:
            for row in csv.DictReader(file):
                symbol = (row.get("Symbol") or "").strip().upper()
                if symbol:
                    tickers[symbol] = (row.get("Security") or symbol).strip()
    return tickers


def load_current_prices():
    """Read optional prices from current_prices.csv (Symbol, CurrentPrice)."""
    prices = {}
    if PRICE_FILE.exists():
        with PRICE_FILE.open("r", newline="", encoding="utf-8-sig") as file:
            for row in csv.DictReader(file):
                symbol = (row.get("Symbol") or "").strip().upper()
                raw_price = (row.get("CurrentPrice") or "").strip()
                if symbol and raw_price:
                    try:
                        price = float(raw_price)
                        if price > 0:
                            prices[symbol] = price
                    except ValueError:
                        print(f"Skipping invalid price for {symbol}: {raw_price}")
    return prices


def ask_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
            if value > 0:
                return value
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Please enter a valid number.")


def ask_quantity():
    while True:
        try:
            value = int(input("Number of shares: ").strip())
            if value > 0:
                return value
            print("Quantity must be a positive whole number.")
        except ValueError:
            print("Please enter a whole number, such as 10.")


def get_position(tickers, prices):
    while True:
        symbol = input("\nStock ticker symbol (or 'done' to finish): ").strip().upper()
        if symbol == "DONE":
            return None
        if not symbol:
            print("Ticker cannot be blank.")
            continue
        if tickers and symbol not in tickers:
            print(f"{symbol} was not found in {TICKER_FILE.name}. Try a listed ticker.")
            continue

        company = tickers.get(symbol, symbol)
        buy_price = ask_positive_number("Buy price per share: ")
        quantity = ask_quantity()

        if symbol in prices:
            current_price = prices[symbol]
            print(f"Using {symbol} current price from {PRICE_FILE.name}: {current_price:.2f}")
        else:
            print(f"No current price found for {symbol}.")
            current_price = ask_positive_number("Enter current market price per share: ")

        return {
            "symbol": symbol,
            "company": company,
            "buy_price": buy_price,
            "quantity": quantity,
            "current_price": current_price,
        }


def calculate(position):
    invested = position["buy_price"] * position["quantity"]
    market_value = position["current_price"] * position["quantity"]
    gain_loss = market_value - invested
    percent = (gain_loss / invested) * 100 if invested else 0
    return invested, market_value, gain_loss, percent


def save_summary(positions):
    """Append one row per holding and a portfolio total to the CSV log."""
    file_exists = OUTPUT_FILE.exists() and OUTPUT_FILE.stat().st_size > 0
    timestamp = datetime.now().astimezone().isoformat(timespec="seconds")
    fields = [
        "Timestamp", "Ticker", "Company", "BuyPrice", "CurrentPrice",
        "Quantity", "InvestedCapital", "MarketValue", "GainLoss", "GainLossPercent"
    ]

    with OUTPUT_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        if not file_exists:
            writer.writeheader()

        total_invested = total_value = 0.0
        for position in positions:
            invested, market_value, gain_loss, percent = calculate(position)
            total_invested += invested
            total_value += market_value
            writer.writerow({
                "Timestamp": timestamp,
                "Ticker": position["symbol"],
                "Company": position["company"],
                "BuyPrice": f'{position["buy_price"]:.2f}',
                "CurrentPrice": f'{position["current_price"]:.2f}',
                "Quantity": position["quantity"],
                "InvestedCapital": f"{invested:.2f}",
                "MarketValue": f"{market_value:.2f}",
                "GainLoss": f"{gain_loss:.2f}",
                "GainLossPercent": f"{percent:.2f}",
            })

        total_gain = total_value - total_invested
        total_percent = (total_gain / total_invested * 100) if total_invested else 0
        writer.writerow({
            "Timestamp": timestamp,
            "Ticker": "PORTFOLIO_TOTAL",
            "Company": "All holdings",
            "BuyPrice": "",
            "CurrentPrice": "",
            "Quantity": sum(p["quantity"] for p in positions),
            "InvestedCapital": f"{total_invested:.2f}",
            "MarketValue": f"{total_value:.2f}",
            "GainLoss": f"{total_gain:.2f}",
            "GainLossPercent": f"{total_percent:.2f}",
        })

    return total_invested, total_value, total_value - total_invested


def main():
    print("=" * 58)
    print("             INVESTMENT PORTFOLIO TRACKER")
    print("=" * 58)
    tickers = load_tickers()
    prices = load_current_prices()
    if tickers:
        print(f"Loaded {len(tickers)} ticker symbols from {TICKER_FILE.name}.")
    else:
        print("Ticker directory not found; ticker validation is disabled.")
    print(f"Loaded {len(prices)} current prices from {PRICE_FILE.name}.")

    positions = []
    while True:
        position = get_position(tickers, prices)
        if position is None:
            break
        positions.append(position)
        print(f"Added {position['symbol']}.")

    if not positions:
        print("\nNo holdings entered. Nothing to save.")
        return

    print("\n" + "=" * 80)
    print(f"{'TICKER':<10}{'QUANTITY':>10}{'INVESTED':>14}{'MARKET VALUE':>16}{'GAIN/LOSS':>14}{'RETURN':>12}")
    print("-" * 80)
    for position in positions:
        invested, market_value, gain_loss, percent = calculate(position)
        print(
            f"{position['symbol']:<10}{position['quantity']:>10}"
            f"{invested:>14.2f}{market_value:>16.2f}"
            f"{gain_loss:>14.2f}{percent:>11.2f}%"
        )

    invested, value, gain = save_summary(positions)
    percent = (gain / invested * 100) if invested else 0
    print("-" * 80)
    print(f"Total invested capital : {invested:.2f}")
    print(f"Current portfolio value: {value:.2f}")
    print(f"Overall gain/loss      : {gain:.2f} ({percent:.2f}%)")
    print(f"\n Summary appended to: {OUTPUT_FILE}")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nProgram cancelled.")
