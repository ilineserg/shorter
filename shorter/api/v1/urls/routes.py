from urllib.parse import unquote

from fastapi import APIRouter
from fastapi import Query
from fastapi import HTTPException
from fastapi import Depends
from fastapi import status

from shorter.context import get_urls_service
from shorter.dto import ShortUrl as ShortUrlDTO
from shorter.dto import SourceUrl as SourceUrlDTO
from shorter.services.urls import UrlsService
from .models import ShortUrl
from .models import ShortUrlCreate
from .models import ShortUrlView
from .models import SourceUrl
from .models import SourceUrlView
from .models import OperationStatus


router = APIRouter(
    prefix='/short_url',
    tags=['short_url'],
)


def get_short_url_query(url: str = Query(...)) -> ShortUrl:
    return ShortUrl(unquote(url))


@router.post(
    "/",
    response_model=ShortUrlView,
    operation_id='create-short-url',
    status_code=status.HTTP_201_CREATED,
)
async def create_short_url(
    create_data: ShortUrlCreate,
    urls_service: UrlsService = Depends(get_urls_service)
) -> ShortUrlView:
    short_url_dto = await urls_service.create_short_url(
        source_url=SourceUrlDTO(create_data.url),
    )
    return ShortUrlView(
        url=ShortUrl(short_url_dto),
    )


@router.delete(
    "/",
    response_model=None,
    operation_id='delete-short-url',
)
async def delete_short_url(
    short_url: ShortUrl = Depends(get_short_url_query),
    urls_service: UrlsService = Depends(get_urls_service)
) -> OperationStatus:
    await urls_service.delete_short_url(
        short_url=ShortUrlDTO(short_url)
    )
    return OperationStatus(ok=True)


@router.get(
    "/",
    response_model=SourceUrlView,
    operation_id='get-source-url',
)
async def get_source_url(
    short_url: ShortUrl = Depends(get_short_url_query),
    urls_service: UrlsService = Depends(get_urls_service)
) -> SourceUrlView:
    source_url_dto = await urls_service.get_source_url(
        short_url=ShortUrlDTO(short_url)
    )
    if source_url_dto is None:
        raise HTTPException(status_code=404, detail="Url not found")
    return SourceUrlView(
        url=SourceUrl(source_url_dto),
    )
