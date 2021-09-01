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

from typing import Optional

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
    "nekos",
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
)


class Result:
    """Represents an image result from the API.

    Attributes
    ----------
    url: Optional[str]
        The image url.
    artist_href: Optional[str]
        The artist's page URL.
    artist_name: Optional[str]
        The artist's name.
    source_url: Optional[str]
        The original link of this image.
    """

    def __init__(self, data: dict):
        self.url: Optional[str] = data.get("url")
        self.artist_href: Optional[str] = data.get("artist_href")
        self.artist_name: Optional[str] = data.get("artist_name")
        self.source_url: Optional[str] = data.get("source_url")

    def __repr__(self) -> str:
        return f"<Result url={self.url} artist_href={self.artist_href} artist_name={self.artist_name} source_url={self.source_url}>"
