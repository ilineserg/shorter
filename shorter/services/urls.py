from typing import Optional

from shorter.dto import SourceUrl, ShortUrl
from shorter.repositories import UrlsRepository
from .base import BaseService
from ..config import SHORT_URL_TEMPLATE
from ..utils import make_random_string


class UrlsService(BaseService):
    def __init__(self, repository: UrlsRepository) -> None:
        super().__init__(repository=repository)

    async def create_short_url(self, source_url: SourceUrl) -> ShortUrl:
        short_url = SHORT_URL_TEMPLATE.substitute(
            slug=make_random_string(8),
        )
        url_dto = await self.repository.add(
            source_url=source_url,
            short_url=short_url,
        )
        return url_dto.short_url

    async def get_source_url(self, short_url: ShortUrl) -> Optional[SourceUrl]:
        url_dto = await self.repository.get_one(short_url=short_url)
        return url_dto.source_url if url_dto else None

    async def delete_short_url(self, short_url: ShortUrl) -> None:
        await self.repository.delete(short_url=short_url)
