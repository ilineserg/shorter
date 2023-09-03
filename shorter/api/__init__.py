from fastapi import FastAPI

from .v1 import urls_router


def create_application() -> FastAPI:
    application = FastAPI(title='URL shorter')
    application.include_router(urls_router)
    return application


app = create_application()


__all__ = ('app', )
