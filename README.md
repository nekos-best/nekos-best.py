# nekos-best.py

[![PyPI](https://img.shields.io/pypi/v/nekosbest?style=flat-square)](https://pypi.org/project/nekosbest)

A simple async Python wrapper for [nekos.best](https://nekos.best) API.

Join the official Discord server [here](https://nekos.best/discord?ref=py).

## Requirements

- aiohttp (>=3.6.2)

## Installation

Make sure to have pip installed in your environement. It will also install all requirements.

```bash
pip install nekosbest
```

## Example

```py
import asyncio
from nekosbest import Client

client = Client()


async def get_single_image(category: str):
    result = await client.get_image(category)
    print(result)


async def get_multiple_images(category: str, amount: int):
    result = await client.get_image(category, amount)
    print(result)


loop = asyncio.get_event_loop()
loop.run_until_complete(get_single_image("nekos"))
# <Result url=https://nekos.best/nekos/0162.png>
loop.run_until_complete(get_multiple_images("nekos", 5))
# <Result url=['https://nekos.best/nekos/0277.png', 'https://nekos.best/nekos/0339.png', 'https://nekos.best/nekos/0391.png', 'https://nekos.best/nekos/0245.png', 'https://nekos.best/nekos/0225.png']>
```

## Migrate from 0.x.x to 1.0.0

`Client.teardown` has been removed, it is no longer needed to pass it when closing.
