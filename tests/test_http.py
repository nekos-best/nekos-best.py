# tests/test_http.py
import pytest
from aioresponses import aioresponses

from nekosbest.http import HttpClient


async def test_session_is_none_before_first_request():
    http = HttpClient()
    assert http.session is None


async def test_session_created_on_first_get_and_reused():
    http = HttpClient()
    with aioresponses() as mocked:
        mocked.get(
            "https://nekos.best/api/v2/neko",
            payload={"results": [{"url": "http://x"}]},
        )
        mocked.get(
            "https://nekos.best/api/v2/neko",
            payload={"results": [{"url": "http://x"}]},
        )
        await http.get("neko", 1)
        session_after_first = http.session
        await http.get("neko", 1)
        assert http.session is session_after_first
    await http.close()


async def test_close_closes_the_session():
    http = HttpClient()
    with aioresponses() as mocked:
        mocked.get(
            "https://nekos.best/api/v2/neko",
            payload={"results": [{"url": "http://x"}]},
        )
        await http.get("neko", 1)
    assert http.session is not None
    await http.close()
    assert http.session.closed


async def test_close_is_idempotent():
    http = HttpClient()
    await http.close()
    await http.close()


async def test_get_after_close_recreates_session():
    http = HttpClient()
    with aioresponses() as mocked:
        mocked.get("https://nekos.best/api/v2/neko", payload={"results": []})
        await http.get("neko", 1)
        first = http.session
        await http.close()
        mocked.get("https://nekos.best/api/v2/neko", payload={"results": []})
        await http.get("neko", 1)
        assert http.session is not first
    await http.close()
