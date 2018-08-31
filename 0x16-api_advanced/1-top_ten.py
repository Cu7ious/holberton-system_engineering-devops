#!/usr/bin/python3
""" This script contains function that queries the Reddit API
    and prints the titles of the first 10 hot posts of a given subreddit.
"""
from requests import get


def top_ten(subreddit):
    """ Queries the Reddit API and prints the titles
        of the first 10 hot posts of a given subreddit.

        Args:
            @subreddit: the subreddit to get the posts from
    """
    url = "https://api.reddit.com/r/{}/hot?limit=10".format(subreddit)
    headers={"User-Agent": "0x16. API advanced by Cu7ious"}
    :q

:Q

    response = get(url, headers=headers, allow_redirects=False)
    if response.status_code is not 200:
        return print(None)

    posts = response.json().get("data").get("children")
    for post in posts:
        print(post.get("data").get("title"))
