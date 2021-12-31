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


class NekosBestBaseError(Exception):
    """Base error of nekosbest client."""


class NotFound(NekosBestBaseError):
    """Raised when API returns a 404."""


class APIError(NekosBestBaseError):
    """Raised when API returns an unexcepted status code."""

    def __init__(self, code: int = None):
        self.code = code


class ClientError(NekosBestBaseError):
    """Raised on Client error."""
