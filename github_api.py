import aiohttp

OWNER = "treshshina-git"
REPO = "donbot_body"
ROOT_FOLDER = "ROMs for Play"


async def get_files(folder: str):
    url = (
        f"https://api.github.com/repos/"
        f"{OWNER}/{REPO}/contents/"
        f"{ROOT_FOLDER}/{folder}"
    )

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:

            print("GitHub URL:", url)
            print("Status:", resp.status)

            data = await resp.json()

            print("Response:", data)

    if not isinstance(data, list):
        raise Exception(
            f"GitHub returned error: {data}"
        )

    return [
        item["name"]
        for item in data
        if item["type"] == "file"
    ]
