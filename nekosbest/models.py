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

import random
from enum import Enum, IntEnum
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .types import ResultType


BASE_URL = "https://nekos.best/api/v2"


class Categories(Enum):
    """Represents the categories of images you can get from the API."""

    # Static images
    neko = "neko"
    kitsune = "kitsune"
    waifu = "waifu"
    husbando = "husbando"

    # Gifs
    baka = "baka"
    bite = "bite"
    blush = "blush"
    bored = "bored"
    cry = "cry"
    cuddle = "cuddle"
    dance = "dance"
    facepalm = "facepalm"
    feed = "feed"
    happy = "happy"
    highfive = "highfive"
    hug = "hug"
    kiss = "kiss"
    laugh = "laugh"
    pat = "pat"
    poke = "poke"
    pout = "pout"
    shrug = "shrug"
    slap = "slap"
    sleep = "sleep"
    smile = "smile"
    smug = "smug"
    stare = "stare"
    think = "think"
    thumbsup = "thumbsup"
    tickle = "tickle"
    wave = "wave"
    wink = "wink"
    handhold = "handhold"
    kick = "kick"
    punch = "punch"
    shoot = "shoot"
    yeet = "yeet"
    nod = "nod"
    nom = "nom"
    nope = "nope"

    @classmethod
    def is_valid(cls, category: str) -> bool:
        """Checks if a category is valid.

        Parameters
        ----------
        category: str
            The category to check.

        Returns
        -------
        bool
            Whether the category is valid.
        """

        return category in cls.__members__

    @classmethod
    def random(cls) -> Categories:
        """Gets a random category."""
        return random.choice(list(cls))


class SearchTypes(IntEnum):
    """Represents the types of search you can do with the API."""

    image = 1
    gif = 2


class CategoryEndpoint:
    """Represents an category endpoint from the API.

    Attributes
    ----------
    category: str
        The category of the endpoint.
    amount: int
        The amount of images to get from the endpoint.
    """

    __slots__ = ("category", "amount")

    def __init__(self, category: str, amount: int = 1):
        self.category: str = category
        self.amount: int = amount

    def __repr__(self) -> str:
        return f"<CategoryEndpoint category={self.category} amount={self.amount}>"

    @property
    def formatted(self) -> str:
        return f"{BASE_URL}/{self.category}?amount={self.amount}"


class SearchEndpoint:
    """Represents an search endpoint from the API.

    Attributes
    ----------
    query: str
        The query to search for.
    type: SearchTypes
        The type of images to return.
    category: str
        The category of the images to return.
    amount: int
        The amount of images to get from the endpoint.
    """

    __slots__ = ("query", "type", "category", "amount")

    def __init__(self, query: str, type: SearchTypes, category: str, amount: int = 1):
        self.query: str = query
        self.type: SearchTypes = type
        self.category: str = category
        self.amount: int = amount

    def __repr__(self) -> str:
        return f"<SearchEndpoint query={self.query} type={self.type} category={self.category} amount={self.amount}>"

    @property
    def formatted(self) -> str:
        return f"{BASE_URL}/search?query={self.query}&type={self.type}&category={self.category}&amount={self.amount}"


class Result:
    """Represents an image result from the API.

    Attributes
    ----------
    url: Optional[str]
        The image / gif URL.
    data: Optional[bytes]
        The image / gif bytes.
    artist_href: Optional[str]
        The artist's page URL.
    artist_name: Optional[str]
        The artist's name.
    source_url: Optional[str]
        The original link of this image.
    anime_name: Optional[str]
        The englified name of the anime the gif was taken from.
    """

    __slots__ = ("url", "artist_href", "artist_name", "source_url", "anime_name", "_data")

    def __init__(self, data: ResultType):
        self.url: Optional[str] = data.get("url")
        self.artist_href: Optional[str] = data.get("artist_href")
        self.artist_name: Optional[str] = data.get("artist_name")
        self.source_url: Optional[str] = data.get("source_url")
        self.anime_name: Optional[str] = data.get("anime_name")
        self._data: ResultType = data

    def __repr__(self) -> str:
        return f"<Result url={self.url} artist_href={self.artist_href} artist_name={self.artist_name} source_url={self.source_url} anime_name={self.anime_name}>"
