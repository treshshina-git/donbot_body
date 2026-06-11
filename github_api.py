import aiohttp

OWNER = "treshshina-git"
REPO = "donbot_body"
ROOT_FOLDER = "ROMs for Play"

async def get_files(folder: str):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{ROOT_FOLDER}/{folder}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()

    return [x["name"] for x in data if x["type"] == "file"]
