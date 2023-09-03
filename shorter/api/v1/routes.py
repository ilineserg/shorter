from fastapi import APIRouter

from .urls.routes import router as urls_router


api_v1_router = APIRouter(prefix='/v1', tags=['v1'])
api_v1_router.include_router(urls_router)
