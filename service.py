from os import getenv

import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

payload = ""
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": "Bearer " + getenv("TOKEN"),
    "X-GitHub-Api-Version": "2022-11-28",
}


class GitHubAPIService:
    @staticmethod
    def get_users_from_API(last_user_id):
        url = f"https://api.github.com/users?per_page=100&since={last_user_id}"
        return requests.request("GET", url, headers=headers, data=payload)
