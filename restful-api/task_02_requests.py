import requests
import json
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post["title"])
    else:
        print("Failed to fetch posts")

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        dict = []
        for post in posts:
            dict.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames = ["id", "title", "body"])
            writer.writeheader()
            writer.writerows(dict)

        print("Posts successfully saved to posts.csv")
    else:
        print("Failed to fetch posts")