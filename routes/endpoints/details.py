import os

import aiohttp
from fastapi import APIRouter, HTTPException

from model.details import Details

route = APIRouter()


@route.get("/markets/{symbol}")
async def market_details(symbol: str):
    url = os.environ.get("DETAILS_URL").format(symbol)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 404:
                raise HTTPException(status_code=400, detail="Invalid symbol")
            if response.status != 200:
                raise HTTPException(status_code=400, detail="Unexpected status code from bittrex")
            return Details.model_validate(await response.json())
