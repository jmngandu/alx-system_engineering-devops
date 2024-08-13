#!/usr/bin/python3
"""
function that queries the Reddit api and returns
number of subcribers (not active, total subscribers)
"""
import json
import requests


def number_of_subscribers(subreddit):
    """return the number of subscribers"""
    url = requests.get("https://www.reddit.com/r/{}/about.json"
                        .format(subreddit), headers={"User-Agent": "mogaka_dev"})
    if url.status_code == 200:
        return url.json().get("data").get("subscribers")
    else:
        return 0
