from typing import Type

from .base import SqlAlchemyRepository
from ..database.models import Url as UrlDB
from ..dto import SourceUrl
from ..dto import ShortUrl
from ..dto import UrlDTO


class UrlsRepository(SqlAlchemyRepository[UrlDB, UrlDTO]):
    def get_db_model_class(self) -> Type[UrlDB]:
        return UrlDB

    def create_object(self, db_object: UrlDB) -> UrlDTO:
        return UrlDTO(
            source_url=SourceUrl(db_object.source_url),
            short_url=ShortUrl(db_object.short_url),
        )

    async def add(self, source_url: SourceUrl, short_url: ShortUrl) -> ShortUrl:
        return await super().add(
            source_url=str(source_url),
            short_url=str(short_url),
        )

    async def get_one(self, short_url: ShortUrl) -> SourceUrl | None:
        return await super().get_one(short_url=str(short_url))

    async def delete(self, short_url: ShortUrl) -> None:
        return await super().delete(short_url=str(short_url))
