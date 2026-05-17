from fastapi import FastAPI, HTTPException

from db import init_db
from operation import get_annual_data

app = FastAPI()

init_db()


@app.get("/symbols/{symbol}/annual/{year}")
def get_symbol_annual(symbol: str, year: str) -> None:
    rows = get_annual_data(symbol, year)
    print("rows type :- ", type(rows))
    print("rows items :- ", rows)

    if not rows:
        # to-do fetch

        # Retry after caching
        rows = get_annual_data(symbol, year)

    if not rows:
        raise HTTPException(
            status_code=404,
            detail="No data found"
        )

    return None
