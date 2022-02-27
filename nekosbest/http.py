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

if TYPE_CHECKING:
    from .types import ResultType


class HttpClient:
    BASE_URL = "https://nekos.best/api/v2"
    DEFAULT_HEADERS = {
        "User-Agent": f"nekosbest.py v{__version__} (Python/{(platform.python_version())[:3]} aiohttp/{aiohttp.__version__})"
    }

    async def get(self, endpoint: str, amount: int, **kwargs) -> ResultType:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"{self.BASE_URL}/{endpoint}",
                    params={"amount": amount} if amount > 1 else {},
                    headers=self.DEFAULT_HEADERS,
                ) as resp:
                    if resp.status == 404:
                        raise NotFound()
                    if resp.status != 200:
                        raise APIError(resp.status)
                    return await resp.json(content_type=None)
        except aiohttp.ClientConnectionError:
            raise ClientError()
