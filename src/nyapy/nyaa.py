import re

from bs4 import BeautifulSoup

from .client import get_client
from .enums import NyaaSite
from .types.nyaa import ContentData, ResponseData


class BadResponse(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class Nyaa:
    def __init__(self, site: NyaaSite) -> None:
        self.client = get_client(site)

    async def get_content(
        self, *, filter, category, query, sort, order, page
    ) -> ResponseData:
        if sort == 'date':
            sort = 'id'

        res = await self.client.get(
            '',
            params={
                'f': filter,
                'c': category,
                'q': query,
                'p': page,
                's': sort,
                'o': order,
            },
        )

        if res.status_code != 200:
            raise BadResponse('Nyaa error')

        html = BeautifulSoup(res.text, 'html.parser')
        rows = html.select('tbody tr')
        data: list[ContentData] = []

        for row in rows:
            properties = row.find_all('td')
            category_row = properties[0].find('a')
            category_row = (category_row or {}).get('title', '')
            comments = properties[1].find('a', attrs={'class': 'commentss'})
            comments = int(comments.text) if comments else 0
            name = properties[1].find('a', {'class': False})
            (name, id) = (name.text, name.get('href')) if name else ('', '')
            id = re.search(r'\d+', (str(id) or ''))
            id = id.group(0) if id else 0
            torrent = properties[2].find('i', {'class': 'fa-download'})
            torrent = torrent.parent if torrent else None
            torrent = torrent.get('href') if torrent else None
            torrent = str(self.client.base_url)[:-1] + str(torrent) if torrent else None
            magnet = properties[2].find('i', {'class': 'fa-magnet'})
            magnet = magnet.parent if magnet else None
            magnet = str(magnet.get('href')) if magnet else None
            size = properties[3].text
            date = properties[4].get('data-timestamp')
            seeders = int(properties[5].text)
            leechers = int(properties[6].text)
            downloads = int(properties[7].text)

            content: ContentData = {
                'id': int(id),
                'category': str(category_row),
                'name': str(name),
                'comments': comments,
                'links': {'torrent': torrent, 'magnet': magnet},
                'size': str(size),
                'date': str(date),
                'seeders': seeders,
                'leechers': leechers,
                'downloads': downloads,
            }

            data.append(content)

        return {'page': page, 'results': len(data), 'data': data}

    async def close(self):
        """Closes connection to nyaa"""
        await self.client.aclose()
