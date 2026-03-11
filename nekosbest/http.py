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

import sys
from typing import TYPE_CHECKING

import aiohttp

from nekosbest import __version__

from .errors import APIError, ClientError, NotFound

if TYPE_CHECKING:
    from .types import ResultType



class HttpClient:
    BASE_URL = "https://nekos.best/api/v2"

    # Old implementation used to truncate 3.14 to 3.1
    _platform_python_version = f"{sys.version_info.major}.{sys.version_info.minor}"

    DEFAULT_HEADERS = {
        "User-Agent": f"nekosbest.py v{__version__} (Python/{_platform_python_version} aiohttp/{aiohttp.__version__})"
    }

    def __init__(self):
        # Connection pooling
        self.session = None

    async def close(self):
        if self.session and not self.session.closed:
            await self.session.close()

    async def get(self, endpoint: str, amount: int, **kwargs) -> ResultType:

        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()

        try:
            async with self.session.get(
                f"{self.BASE_URL}/{endpoint}",
                params={"amount": amount} if amount > 1 else {},
                headers=self.DEFAULT_HEADERS,
            ) as resp:
                if resp.status == 404:
                    raise NotFound()
                if resp.status != 200:
                    raise APIError(resp.status)
                return await resp.json(content_type=None)

        # Context
        except aiohttp.ClientConnectionError as exc:
            raise ClientError("Failed to connect to API.") from exc
