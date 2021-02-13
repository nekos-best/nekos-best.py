# nekos-best.py

A simple async Python wrapper for [nekos.best](https://nekos.best) API.

Join the official Discord server [here](https://discord.gg/2NsE7akmM5).

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

async def main(category: str):
    result = await client.get_image(category)
    print(result)
    print(result.url)
    await client.teardown()  # Cleanup http client.

loop = asyncio.get_event_loop()
loop.run_until_complete(main("nekos"))  # https://nekos.best/nekos/0001.png
```
