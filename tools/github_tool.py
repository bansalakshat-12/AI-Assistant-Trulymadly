import requests

GITHUB_API_URL = "https://api.github.com/search/repositories"


def search_repositories(query: str, limit: int = 3):
   
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc"
    }


    response = requests.get(GITHUB_API_URL, params=params)


    response.raise_for_status()


    data = response.json()


    repositories = data.get("items", [])


    results = []

    for repo in repositories[:limit]:
        results.append({
            "name": repo.get("name"),
            "description": repo.get("description"),
            "stars": repo.get("stargazers_count"),
            "url": repo.get("html_url")
        })

    return results
