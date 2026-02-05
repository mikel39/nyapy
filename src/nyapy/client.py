from httpx import AsyncClient, AsyncHTTPTransport


def get_client(base_url: str) -> AsyncClient:
    return AsyncClient(
        base_url=base_url,
        headers={
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36'
        },
        timeout=10.0,
        transport=AsyncHTTPTransport(retries=10),
    )
