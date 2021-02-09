# nekos-best.py

A simple async Python wrapper for nekos.best API.

> Supported categories are: cuddle, feed, hug, kiss, nekos, pat, poke, slap and tickle.<br>
> See <https://nekos.best/endpoints> for all endpoints.

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
loop.run_until_complete(main("nekos"))
```
