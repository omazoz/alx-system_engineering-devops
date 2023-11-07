#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0'}).json()
    sub = r.get("data", {}).get("subscribers", 0)
    return sub
