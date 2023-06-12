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

from typing import List, Optional

from .errors import InvalidAmount, UnknownCategory
from .http import HttpClient
from .models import Categories, CategoryEndpoint, Result

# TODO: Add Ruff


class Client:
    """Client to make requests to nekos.best API."""

    def __init__(self) -> None:
        self.http: HttpClient = HttpClient()

    async def close(self) -> None:
        """Closes the client."""
        await self.http.session.close()

    async def fetch(self, category: Optional[Categories] = None, amount: int = 1) -> List[Result]:
        """Returns one or multiple images URLs of a specific category along with their metadata.

        Parameters
        ----------
        category: Optional[Categories]
            The category of image you want to get.
            If not specified, it will return a random image.
            Defaults to None which therefore will be a random image.
        amount: int
            The amount of images. Must be between 1 and 20.
            Defaults to 1.

        Returns
        -------
        List[Result]
        """
        if category is None:
            category = Categories.random()

        if not Categories.is_valid(category):
            raise UnknownCategory(
                f"This isn't a valid category. It must be one of the following: {', '.join(Categories.__members__)}."
            )
        if not 1 <= amount <= 20:
            raise InvalidAmount("Amount parameter must be between 1 and 20.")

        endpoint = CategoryEndpoint(category, amount)
        response = await self.http.get_results(endpoint)
        return [Result(result) for result in response["results"]]

    async def fetch_file(
        self, category: Optional[Categories] = None, amount: int = 1
    ) -> List[Result]:
        """Returns one or multiple images bytes of a specific category along with their metadata.

        Parameters
        ----------
        category: Optional[Categories]
            The category of image you want to get.
            If not specified, it will return a random image.
            Defaults to None which therefore will be a random image.
        amount: int
            The amount of images. Must be between 1 and 20.
            Defaults to 1.

        Returns
        -------
        List[Result]
        """
        # TODO
