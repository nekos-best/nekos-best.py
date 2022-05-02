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

from typing import TYPE_CHECKING, Optional


if TYPE_CHECKING:
    from .types import ResultType

CATEGORIES = (
    "baka",
    "bite",
    "blush",
    "bored",
    "cry",
    "cuddle",
    "dance",
    "facepalm",
    "feed",
    "happy",
    "highfive",
    "hug",
    "kiss",
    "laugh",
    "neko",
    "pat",
    "poke",
    "pout",
    "shrug",
    "slap",
    "sleep",
    "smile",
    "smug",
    "stare",
    "think",
    "thumbsup",
    "tickle",
    "wave",
    "wink",
    "kitsune",
    "waifu",
    "handhold",
    "kick",
    "punch",
    "shoot",
)


class Result:
    """Represents an image result from the API.

    Attributes
    ----------
    url: Optional[str]
        The image / gif URL.
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
