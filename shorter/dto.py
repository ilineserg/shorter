import dataclasses
from typing import NewType

SourceUrl = NewType('SourceUrl', str)
ShortUrl = NewType('ShortUrl', str)


@dataclasses.dataclass(frozen=True)
class UrlDTO:
    source_url: SourceUrl
    short_url: ShortUrl

