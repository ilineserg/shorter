from typing import NewType

from pydantic import AnyHttpUrl
from pydantic import BaseModel


ShortUrl = NewType('ShortUrl', AnyHttpUrl)
SourceUrl = NewType('SourceUrl', AnyHttpUrl)


class ShortUrlCreate(BaseModel):
    url: SourceUrl


class ShortUrlView(BaseModel):
    url: ShortUrl


class SourceUrlView(BaseModel):
    url: SourceUrl


class OperationStatus(BaseModel):
    ok: bool
