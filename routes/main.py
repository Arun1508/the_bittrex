from fastapi import APIRouter, Depends

from routes.endpoints import details, summary
from utils.user_auth import get_current_username

routes = APIRouter()

routes.include_router(
    summary.route, tags=["Summary"], dependencies=[Depends(get_current_username)]
)
routes.include_router(
    details.route, tags=["Details"], dependencies=[Depends(get_current_username)]
)
