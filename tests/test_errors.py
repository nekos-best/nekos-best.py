import aiohttp
import pytest
from aioresponses import aioresponses

from nekosbest.errors import APIError, ClientError, NotFound
from nekosbest.http import HttpClient


def test_api_error_has_descriptive_message_with_code():
    err = APIError(500)
    assert str(err) == "nekos.best API returned unexpected status code 500."
    assert err.code == 500


def test_api_error_has_descriptive_message_without_code():
    err = APIError()
    assert "unexpected status code" in str(err).lower()
    assert err.code is None


def test_api_error_preserves_code_attribute():
    assert APIError(418).code == 418
    assert APIError(None).code is None


async def test_client_error_chains_from_aiohttp_connection_error():
    http = HttpClient()
    with aioresponses() as mocked:
        mocked.get(
            "https://nekos.best/api/v2/neko",
            exception=aiohttp.ClientConnectionError("boom"),
        )
        with pytest.raises(ClientError) as excinfo:
            await http.get("neko", 1)
    assert excinfo.value.__cause__ is not None
    assert isinstance(excinfo.value.__cause__, aiohttp.ClientConnectionError)
    await http.close()


async def test_not_found_is_raised_on_404():
    http = HttpClient()
    with aioresponses() as mocked:
        mocked.get("https://nekos.best/api/v2/neko", status=404)
        with pytest.raises(NotFound):
            await http.get("neko", 1)
    await http.close()
