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


class Categories(Enum):
    cuddle = "cuddle"
    feed = "feed"
    hug = "hug"
    kiss = "kiss"
    nekos = "nekos"
    pat = "pat"
    poke = "poke"
    slap = "slap"
    tickle = "tickle"

    @classmethod
    def has_value(cls, value: str):
        return value in cls.__members__


class Result:
    def __init__(self, data: dict):
        self.url = data.get("url")
