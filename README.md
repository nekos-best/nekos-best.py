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
from typing import Union

from nekosbest import Client, Result

client = Client()


async def get_img(type: str, amount: int = 1) -> Union[Result, list[Result]]:
    result = await client.get_image(type, amount)
    print(result)

loop = asyncio.get_event_loop()

loop.run_until_complete(get_img("nekos"))
# <Result url=https://nekos.best/api/v1/nekos/0356.jpg artist_href=https://www.pixiv.net/en/users/38378485 artist_name=奥馬 source_url=https://www.pixiv.net/en/artworks/88188062>
loop.run_until_complete(get_img("nekos", 2))
# [<Result url=https://nekos.best/api/v1/nekos/0072.jpg artist_href=https://www.pixiv.net/en/users/12191 artist_name=こみやひとま source_url=https://www.pixiv.net/en/artworks/66834141>, <Result url=https://nekos.best/api/v1/nekos/0215.jpg artist_href=https://www.pixiv.net/en/users/3684923 artist_name=ひゅらさん source_url=https://www.pixiv.net/en/artworks/79697176>]

```

## Breaking changes

### Migrate from 0.x.x to 1.0.0

`Client.teardown` has been removed, it is no longer needed to pass it when closing.

### Migrate from 1.0.20 to 1.1.0

`nekosbest.Result.source_details` has been removed. Source details are now in `Result`.  
And therefore, `nekosbest.Results` and `nekosbest.SourceDetails` got removed too.
