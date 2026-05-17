# Market Data REST API

A simple REST API built with **FastAPI** that fetches market data from the Alpha Vantage API, caches monthly stock data locally in **SQLite**, and serves aggregated annual market statistics.

The API follows a **cache-first strategy**:

1. Check local SQLite database
2. If data exists → return aggregated result
3. If data does not exist:
   - Fetch from Alpha Vantage
   - Store monthly data in SQLite
   - Aggregate yearly statistics
   - Return response

---

## Features

- REST API using FastAPI
- Integration with Alpha Vantage monthly market data API
- SQLite local caching (without ORM)
- Automatic cache population
- Annual aggregation from monthly records
- SQL-based aggregation for better performance

---

## Tech Stack

- Python 3.11.2(above 3.11)
- FastAPI
- SQLite (`sqlite3`)
- Requests
- Uvicorn

---

## Project Structure

```txt
market_api/
│
├── .gitignore
├── .env
├── app.py
├── operations.py
├── requirements.txt
├── db.py
├── README.md
└── market_data.db
```

---

## Installation and configuration

Clone the repository:

```bash
git clone <repository-url>

cd market_api
```

Create virtual environment with pyenv:

```bash
pyenv install 3.11.2
pyenv virtualenv 3.11.2 fast_api

```

Activate environment:

Linux / Mac:

```bash
pyenv activate fast_api
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---
## Environment Configuration

Create a `.env` file:

```env
API_KEY=YOUR_API_KEY
```

Example:

```env
API_KEY=abc123456
```
---


Get API key from:

https://www.alphavantage.co/support/#api-key

---

## Run Application

Start server:

```bash
uvicorn app:app --reload
```

Server runs on:

```txt
http://localhost:8000
```



---

## API Endpoint

### Get Annual Market Statistics

```http
GET /symbols/{symbol}/annual/{year}
```

Example:

```http
GET /symbols/IBM/annual/2005
```

Response:

```json
{
    "high": "80.8700",
    "low": "76.0600",
    "volume": "139457800"
}
```

---

Annual calculation:

```text
high = MAX(monthly highs)

low = MIN(monthly lows)

volume = SUM(monthly volumes)
```

Result:

```json
{
    "high": 90,
    "low": 50,
    "volume": 600
}
```

---

## Example Request Flow



Sample request:

```http
GET /symbols/IBM/annual/2005
```

## Author

Perera N .P .J