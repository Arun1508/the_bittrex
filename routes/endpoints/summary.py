import os

import aiohttp
from fastapi import APIRouter, HTTPException

from model.summary import SummaryResponse

route = APIRouter()


@route.get("/summary", response_model=SummaryResponse)
async def summary():
    url = os.environ.get("SUMMARY_URL")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                raise HTTPException(status_code=400, detail="Unexpected status code")
            data = {}
            data["summary"] = await response.json()
            return SummaryResponse.model_validate(data)
