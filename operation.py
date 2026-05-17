from db import get_connection


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
