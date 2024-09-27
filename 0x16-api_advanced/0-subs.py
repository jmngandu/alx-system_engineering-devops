#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;\
                         rv:68.0) Gecko/20100101 FirefoxFirefox/68.0'}
    with requests.session() as client:
        info = client.get(url, headers=headers, allow_redirects=False).json()
        try:
            return info.get('data', {}).get('subscribers', 0)
        except Exception:
            return 0
