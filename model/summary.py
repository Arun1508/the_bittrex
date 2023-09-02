from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from model.details import Details


class SummaryResponse(BaseModel):
    summary: Optional[List[Details]]
    model_config = ConfigDict(fromattributes=True)
