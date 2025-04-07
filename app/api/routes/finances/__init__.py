from app import api

from .finances import router

api.include_router(router)
