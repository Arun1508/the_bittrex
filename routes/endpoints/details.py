import os

import aiohttp
from fastapi import APIRouter, HTTPException

from model.details import DetailsResponse

route = APIRouter()


@route.get("/markets/{symbol}")
async def market_details(symbol: str) -> DetailsResponse:
    """
    Get details for a particular market
    Args: symbol: Symbol of the market. This will be passed during api call to bittrex
    Return: Details Response class object.
    """
    url = os.environ.get("DETAILS_URL").format(symbol)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 404:
                raise HTTPException(status_code=400, detail="Invalid symbol")
            if response.status != 200:
                raise HTTPException(status_code=400, detail="Unexpected status code from bittrex")
            return DetailsResponse.model_validate(await response.json())
