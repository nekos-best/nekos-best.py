# nekos-best.py

[![PyPI](https://img.shields.io/pypi/v/nekosbest?style=flat-square)](https://pypi.org/project/nekosbest)

A simple async Python wrapper for [nekos.best](https://nekos.best) API.

Join the official Discord server [here](https://nekos.best/discord?ref=py).

## Requirements

- aiohttp (>=3.6.2)

## Installation

Make sure to have pip installed in your environement. It will also install all requirements.

```bash
pip install -U nekosbest
```

## Example

```py
import asyncio

from nekosbest import Client


async def main() -> None:
    client = Client()
    try:
        single = await client.get_image("neko")
        print(single)
        multiple = await client.get_image("neko", 3)
        print(multiple)
    finally:
        await client.close()


asyncio.run(main())
```

## Recommended usage

Use `Client` as an async context manager so the underlying HTTP session is always closed cleanly, even if an error is raised:

```py
import asyncio

from nekosbest import Client


async def main() -> None:
    async with Client() as client:
        result = await client.get_image("neko")
        print(result.url)
        if result.dimensions is not None:
            print(result.dimensions.width, result.dimensions.height)


asyncio.run(main())
```

## Exception handling

All exceptions raised by the library inherit from `NekosBestBaseError`. The most common ones you may want to catch:

- `NotFound` — the requested category did not exist on the API.
- `APIError` — the API returned an unexpected non-2xx status. The status code is available on `err.code`.
- `ClientError` — the HTTP client could not reach the API (DNS failure, timeout, connection reset, ...). The underlying `aiohttp.ClientConnectionError` is preserved on `err.__cause__`.

```py
from nekosbest import APIError, Client, ClientError, NotFound


async def fetch(client: Client, category: str) -> None:
    try:
        result = await client.get_image(category)
    except NotFound:
        print(f"unknown category: {category}")
    except APIError as err:
        print(f"nekos.best returned {err.code}")
    except ClientError as err:
        print(f"could not reach nekos.best: {err.__cause__}")
    else:
        print(result.url)
```

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for the full release history, including
migration notes for every breaking change.
