#!/usr/bin/python3
""" This script contains the function that queries the Reddit API
    and returns a list containing the titles of all hot articles
    for a given subreddit.
"""
from requests import get


def recurse(subreddit, hot_list=[], after=""):
    """ This script contains the function that queries the Reddit API
        and returns a list containing the titles of all hot articles
        for a given subreddit.

        Args:
            @subreddit: the subreddit to get the titles from

        Returns: the titles of all hot articles for a given subreddit, list
                 None if no results are found, None
    """
    url = "https://api.reddit.com/r/{}/hot?after={}".format(subreddit, after)
    headers = {"User-Agent": "0x16. API advanced by Cu7ious"}

    response = get(url, headers=headers, allow_redirects=False)
    if response.status_code is not 200:
        return None

    posts = response.json().get("data").get("children")
    for post in posts:
        hot_list.append(post.get("data").get("title"))

    after = response.json().get("data").get("after")
    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)
