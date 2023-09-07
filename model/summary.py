from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from model.details import DetailsResponse


class SummaryResponse(BaseModel):
    """Response model for Summary APIs"""

    summary: Optional[List[DetailsResponse]]
    model_config = ConfigDict(fromattributes=True)
