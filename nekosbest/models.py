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

import urllib.parse
from typing import List, Optional

CATEGORIES = (
    "baka",
    "cry",
    "cuddle",
    "dance",
    "feed",
    "hug",
    "kiss",
    "laugh",
    "nekos",
    "pat",
    "poke",
    "slap",
    "smile",
    "smug",
    "tickle",
    "wave",
)


class SourceDetails:
    """Represents an image source.

    Attributes
    ----------
    artist_href: Optional[str]
        The artist's page URL.
    artist_name: Optional[str]
        The artist's name.
    source_url: Optional[str]
        The original link of this image.
    """

    def __init__(self, data: dict):
        artist_href, artist_name, source_url = (
            data.get("artist_href"),
            data.get("artist_name"),
            data.get("source_url"),
        )
        self.artist_href: Optional[str] = (
            urllib.parse.unquote(artist_href) if artist_href else None
        )
        self.artist_name: Optional[str] = (
            urllib.parse.unquote(artist_name) if artist_href else None
        )
        self.source_url: Optional[str] = urllib.parse.unquote(source_url) if artist_href else None

    def __repr__(self) -> str:
        return f"<SourceDetails artist_href={self.artist_href} artist_name={self.artist_name} source_url={self.source_url}>"


class Result:
    """Represents a single entry response from the API.

    Attributes
    ----------
    url: Optional[str]
        The image url.
    source_details: Optional[nekosbest.SourceDetails]
        The image source details.
    """

    def __init__(self, data: dict):
        self.url: Optional[str] = data.get("url")
        source_details = data.get("details", {})
        self.source_details: Optional[SourceDetails] = (
            SourceDetails(source_details) if source_details else None
        )

    def __repr__(self) -> str:
        return f"<Result url={self.url} source_details={self.source_details}>"


class Results:
    """Represents a multiple entries response from the API.

    Attributes
    ----------
    url: Optional[List[str]]
        The images urls.
    source_details: Optional[List[nekosbest.SourceDetails]]
        The images source details.
    """

    def __init__(self, data: dict):
        self.url: Optional[List[str]] = data.get("url")
        source_details = data.get("details", [])
        self.source_details: Optional[List[SourceDetails]] = (
            [SourceDetails(k) for k in source_details] if source_details else None
        )

    def __repr__(self) -> str:
        return f"<Results url={self.url} source_details={self.source_details}>"
