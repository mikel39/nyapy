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
type Filter = Literal['no_remakes', 'trusted_only']
type SukebeiCategories = Literal[
    'art',
    'art_anime',
    'art_doujinshi',
    'art_games',
    'art_manga',
    'art_pictures',
    'real_life',
    'real_life_pictures',
    'real_life_videos',
]
type NyaaFunCategories = Literal[
    'anime',
    'anime_amv',
    'anime_english',
    'anime_non_english',
    'anime_raw',
    'audio',
    'audio_lossless',
    'audio_lossy',
    'literature',
    'literature_english',
    'literature_non_english',
    'literature_raw',
    'live_action',
    'live_action_english',
    'live_action_idol_pv',
    'live_action_non_english',
    'live_action_raw',
    'pictures',
    'pictures_graphics',
    'pictures_photos',
    'software',
    'software_apps',
    'software_games',
]
