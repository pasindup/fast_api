import requests
from db import get_connection

API_KEY = "AU5683G8JJIHEBJH" #personal key.
BASE_URL = "https://www.alphavantage.co/query"


def fetch_and_store_data(symbol: str):
    params = {
        "function": "TIME_SERIES_MONTHLY",
        "symbol": symbol,
        "apikey": API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    monthly_data = data.get("Monthly Time Series", {})

    conn = get_connection()

    for date, values in monthly_data.items():
        conn.execute("""
        INSERT OR IGNORE INTO monthly_market_data (
            symbol,
            date,
            open,
            high,
            low,
            close,
            volume
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            symbol,
            date,
            float(values["1. open"]),
            float(values["2. high"]),
            float(values["3. low"]),
            float(values["4. close"]),
            int(values["5. volume"])
        ))

    conn.commit()
    conn.close()


def get_annual_data(symbol: str, year: str) -> list:
    conn = get_connection()

    rows = conn.execute("""
    SELECT high, low, volume
    FROM monthly_market_data
    WHERE symbol = ?
      AND strftime('%Y', date) = ?
    """, (symbol, year)).fetchall()

    conn.close()

    return rows


def calculate_annual_metrics(rows) -> dict:
    print("rows: ", rows)
    highs = [row["high"] for row in rows]
    lows = [row["low"] for row in rows]
    volumes = [row["volume"] for row in rows]

    return {
        "high": str(max(highs)),
        "low": str(min(lows)),
        "volume": str(sum(volumes))
    }
