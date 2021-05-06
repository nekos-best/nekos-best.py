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

from enum import Enum
from typing import List, Optional, Union

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


class Result:
    """Represents a response from the API.
    
    Attributes
    ----------
    url: Optional[Union[str, List[str]]]
        The image(s) url(s).
    """

    def __init__(self, data: dict):
        self.url: Optional[Union[str, List[str]]] = data.get("url")

    def __repr__(self) -> str:
        return f"<Result url={self.url}>"
