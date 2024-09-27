import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers 

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit,.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "jthree3_globally:v1.0.1 (by /u/jmngandu)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0

    try:
        data = response.json()
        return data["data"]["subscribers"]
    except (KeyError, json.JSONDecodeError):
        return 0
