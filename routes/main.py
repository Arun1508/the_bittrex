from fastapi import APIRouter

from routes.endpoints import details, summary

routes = APIRouter()

routes.include_router(summary.route, tags=["Summary"])
routes.include_router(details.route, tags=["Details"])
