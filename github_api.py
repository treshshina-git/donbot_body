import aiohttp
from urllib.parse import quote

OWNER = "treshshina-git"
REPO = "donbot_body"


async def get_files(folder: str):
    url = (
        "https://api.github.com/repos/"
        "treshshina-git/donbot_body/contents"
    )

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()

    print(data)

    return []
