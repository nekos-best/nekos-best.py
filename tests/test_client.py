import pytest
from aioresponses import aioresponses

from nekosbest import Client


@pytest.mark.asyncio
async def test_async_context_manager_closes_session():
    async with Client() as client:
        with aioresponses() as m:
            m.get(
                "https://nekos.best/api/v2/neko",
                payload={"results": [{"url": "https://x/y.png", "artist_href": "", "artist_name": "", "source_url": ""}]},
            )
            await client.get_image("neko")
        assert client.http.session is not None
        assert not client.http.session.closed
    assert client.http.session is not None
    assert client.http.session.closed


@pytest.mark.asyncio
async def test_bare_client_then_close():
    client = Client()
    with aioresponses() as m:
        m.get(
            "https://nekos.best/api/v2/neko",
            payload={"results": [{"url": "https://x/y.png", "artist_href": "", "artist_name": "", "source_url": ""}]},
        )
        await client.get_image("neko")
    assert client.http.session is not None
    assert not client.http.session.closed
    await client.close()
    assert client.http.session.closed


@pytest.mark.asyncio
async def test_close_without_requests_is_ok():
    client = Client()
    await client.close()  # session is None; must not raise
    assert client.http.session is None
