"""
A simple async Python wrapper for nekos.best API.
Copyright (C) 2021  PredaaA

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

from .http import HttpClient
from .models import CATEGORIES, Result


class Client:
    """Client to make requests to nekos.best API."""

    def __init__(self):
        self.http = HttpClient()

    async def get_image(self, category: str, amount: int = 1) -> Result:
        """
        |coro|

        Returns an image URL of a specific category.

        Parameters
        ----------
        category: str
            The category of image you want to get.
        amount: int
            The amount of images. Must be between 1 and 20.

        Returns
        -------
        nekosbest.Result
        """
        if not category in CATEGORIES:
            raise ValueError("This isn't a valid category.")
        if not 1 <= amount <= 20:
            raise ValueError("Amount parameter must be between 1 and 20.")

        result = await self.http.get(category, amount)
        return Result(result)
