#!/usr/bin/python3
"""Contains recurse function"""
import requests


def recurse(subreddit, articles_list=[], after="", counter=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "0x16-api_advanced:project: v1.0.0"
    }
    params = {
        "after": after,
        "count": counter,
        "limit": 100
    }
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code == 404:
        return None

    results = res.json().get("data")
    after = results.get("after")
    counter += results.get("dist")
    for c in results.get("children"):
        articles_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, articles_list, after, counter)
    return articles_list
