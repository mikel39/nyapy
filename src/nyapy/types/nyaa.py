from typing import Literal, TypedDict


class _Links(TypedDict):
    torrent: str | None
    magnet: str | None


class ContentData(TypedDict):
    id: int
    category: str
    name: str
    comments: int
    size: str
    date: str
    seeders: int
    leechers: int
    downloads: int
    links: _Links


class ResponseData(TypedDict):
    page: int
    results: int
    data: list[ContentData]


type Sort = Literal['comments', 'size', 'date', 'seeders', 'leechers', 'downloads']
type Order = Literal['asc', 'desc']
