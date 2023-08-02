import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_movie(title):
    request_url = f'https://www.omdbapi.com/?t={title}&apikey={os.getenv("API_KEY")}'

    url1 = requests.get(request_url).json()

    return url1


if __name__ == "__main__":
    title = input("enter movie or TV show title: ")

    print(get_movie(title))
