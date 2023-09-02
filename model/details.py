from typing import Optional

from pydantic import BaseModel, ConfigDict


class Details(BaseModel):
    symbol: Optional[str] = ""
    high: Optional[str] = ""
    low: Optional[str] = ""
    volume: Optional[str] = ""
    quoteVolume: Optional[str] = ""
    percentChange: Optional[str] = ""
    updatedAt: Optional[str] = ""

    model_config = ConfigDict(fromattributes=True)
