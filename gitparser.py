import time
from os import getenv

from dotenv import find_dotenv, load_dotenv

from service import GitHubAPIService
from user_service import UserCRUDService

load_dotenv(find_dotenv())


def user_parser():
    last_user_id = UserCRUDService.get_last_user_id()

    while True:
        request = GitHubAPIService.get_users_from_API(last_user_id)

        if request.status_code != 200:
            print(request.text)
            return None

        users = request.json()

        if not users:
            return None

        for user in users:
            if user["login"].count("z") > 2:
                print(user["login"])
                UserCRUDService.create_user(user)

        last_user_id = users[-1]["id"]

        # Otherwise you get banned because of ratelimit of your token
        time.sleep(3600 / int(getenv("RATELIMIT")))


if __name__ == "__main__":
    user_parser()
