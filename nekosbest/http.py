"""
A simple async Python wrapper for nekos.best API.
Copyright (C) 2021-present  PredaaA

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from __future__ import annotations

import platform
from typing import TYPE_CHECKING

import aiohttp

from nekosbest import __version__

from .errors import APIError, ClientError, NotFound
from .models import CategoryEndpoint, SearchEndpoint

if TYPE_CHECKING:
    from .types import ResultType


class HttpClient:
    def __init__(self) -> None:
        self.session: aiohttp.ClientSession = aiohttp.ClientSession(
            headers={
                "User-Agent": f"nekosbest.py v{__version__} (Python/{(platform.python_version())[:3]} aiohttp/{aiohttp.__version__})"
            }
        )

    async def get_results(self, endpoint: CategoryEndpoint) -> ResultType:
        try:
            async with self.session.get(endpoint.formatted) as resp:
                if resp.status == 404:
                    raise NotFound
                if resp.status != 200:
                    raise APIError(resp.status)

                return await resp.json()
        except aiohttp.ClientConnectionError:
            raise ClientError

    async def get_search_results(self, endpoint: SearchEndpoint) -> ResultType:
        ...
        # TODO

    async def get_file(self, image_url: str) -> bytes:
        # Add a idiot proof check here
        try:
            async with self.session.get(image_url) as resp:
                if resp.status != 200:
                    raise APIError(resp.status)

                return await resp.read()
        except aiohttp.ClientConnectionError:
            raise ClientError
