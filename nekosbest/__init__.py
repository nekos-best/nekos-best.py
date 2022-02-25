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

__version__ = "1.1.5"
__author__ = "PredaaA"
__copyright__ = "Copyright 2021-present PredaaA"


from .client import Client as Client
from .errors import (
    APIError as APIError,
    NekosBestBaseError as NekosBestBaseError,
    NotFound as NotFound,
)
from .models import Result as Result
