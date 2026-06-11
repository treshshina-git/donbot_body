import aiohttp
from urllib.parse import quote

OWNER = "treshshina-git"
REPO = "donbot_body"


async def get_files(folder: str):
    path = quote(f"ROMS/{folder}")

    url = (
        f"https://api.github.com/repos/"
        f"{OWNER}/{REPO}/contents/{path}"
    )

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()

    if not isinstance(data, list):
        raise Exception(f"GitHub returned error: {data}")

    return [
        item["name"]
        for item in data
        if item["type"] == "file"
    ]
