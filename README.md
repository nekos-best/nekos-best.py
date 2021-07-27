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

client = Client()


async def get_single_image(category: str):
    result = await client.get_image(category)
    print(result)


async def get_multiple_images(category: str, amount: int):
    result = await client.get_image(category, amount)
    print(result)


loop = asyncio.get_event_loop()
loop.run_until_complete(get_single_image("nekos"))
# <Result url=https://nekos.best/nekos/0338.png source_details=<SourceDetails artist_href=https://www.pixiv.net/en/users/28136401 artist_name=PiAn source_url=https://www.pixiv.net/en/artworks/91363666>>
loop.run_until_complete(get_multiple_images("nekos", 5))
# <Results url=['https://nekos.best/nekos/0351.png', 'https://nekos.best/nekos/0442.png', 'https://nekos.best/nekos/0436.png', 'https://nekos.best/nekos/0307.png', 'https://nekos.best/nekos/0009.png'] source_details=[<SourceDetails artist_href=https://www.pixiv.net/en/users/7331947 artist_name=xoaiu source_url=https://www.pixiv.net/en/artworks/87593460>, <SourceDetails artist_href=https://www.pixiv.net/en/users/37889769 artist_name=タン塩 source_url=https://www.pixiv.net/en/artworks/89459198>, <SourceDetails artist_href=https://www.pixiv.net/en/users/38808847 artist_name=Elliot source_url=https://www.pixiv.net/en/artworks/89283107>, <SourceDetails artist_href=https://www.pixiv.net/en/users/43296648 artist_name=楠シノ source_url=https://www.pixiv.net/en/artworks/86584286>, <SourceDetails artist_href=https://www.pixiv.net/en/users/32933178 artist_name=しずりゆき source_url=https://www.pixiv.net/artworks/85664088>]>
```

## Breaking changes

### Migrate from 0.x.x to 1.0.0

`Client.teardown` has been removed, it is no longer needed to pass it when closing.

### Migrate from 1.0.20 to 1.1.0

`nekosbest.Result.source_details` has been removed. Source details are now in `Result`.  
And therefore, `nekosbest.Results` and `nekosbest.SourceDetails` got removed too.
