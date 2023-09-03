from typing import cast
from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from .config import DATABASE_URI
from .repositories import UrlsRepository
from .services.urls import UrlsService


async_engine = create_async_engine(DATABASE_URI)
async_session_maker = cast(
    Type[AsyncSession],
    async_sessionmaker(async_engine, expire_on_commit=False, autocommit=False),
)


def get_urls_service() -> UrlsService:
    repository = UrlsRepository(session_factory=async_session_maker)
    return UrlsService(repository=repository)
