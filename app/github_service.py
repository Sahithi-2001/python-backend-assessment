import httpx


async def fetch_repo_data(repo_name: str):
    """
    repo_name example: owner/repo
    """
    url = f"https://api.github.com/repos/{repo_name}"

    async with httpx.AsyncClient(timeout=5, follow_redirects=True) as client:
        response = await client.get(url)

    # If repo truly doesn't exist
    if response.status_code == 404:
        return None

    data = response.json()

    return {
        "stars": data.get("stargazers_count", 0),
        "description": data.get("description") or ""
    }
