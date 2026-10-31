# Investment Portfolio Tracker

A command-line Python utility that records stock holdings, calculates investment performance, and appends a report to a CSV file.

## Files
- `portfolio.py` — main application
- `market_prices.csv` — ticker/company directory supplied with the project (used to validate symbols; it does **not** contain stock prices)
- `current_prices.csv` — editable ticker-to-current-price file
- `portfolio_summary.csv` — created automatically after a portfolio is entered

## Requirements
- Python 3.8 or newer
- No third-party packages required (uses Python's built-in `csv` module)

## Run
Open a terminal in this folder and execute:

```bash
python portfolio.py
```

Enter each ticker, buy price per share, and number of shares. If a current price exists in `current_prices.csv`, it is used automatically. Otherwise, the program asks you to enter the current market price manually. Type `done` when finished.

## Update market prices
Edit `current_prices.csv` using this format:

```csv
Symbol,CurrentPrice
AAPL,225.50
MSFT,510.25
```

Replace the sample values with current prices before running. The supplied `market_prices.csv` is only a list of ticker symbols and company names, not a price feed. The program does not fetch live prices from the internet.

## Output
`portfolio_summary.csv` is created/appended automatically. It includes a timestamp, each holding's invested capital, market value, gain/loss and percentage return, plus a portfolio total row. Currency values use the same currency/unit as the prices you enter.
