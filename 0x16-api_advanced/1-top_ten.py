#!/usr/bin/python3
"""this module contains top_ten function"""
import requests


def top_ten(subreddit):
    """Prints the titles of the 10 hottest posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "0x16-api_advanced:project: v1.0.0"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    for c in results.get("children"):
        print(c.get("data").get("title"))
