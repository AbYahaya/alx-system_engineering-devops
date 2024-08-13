#!/usr/bin/python3
"""
AB Yahaya
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit. If no results are found or the
    subreddit is invalid, returns None.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): Accumulator for titles of hot articles.
        after (str): The 'after' parameter for pagination.

    Returns:
        list: A list containing the titles of all hot articles, or None if the subreddit is invalid.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
        'User-Agent': 'python-requests/2.28.1'  # Standard User-Agent header
    }
    params = {'after': after}  # No limit specified, using API's default (typically 25)

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            children = data.get('children', [])
            if not children and not hot_list:
                return None  # No posts found for the subreddit

            for child in children:
                hot_list.append(child['data']['title'])

            after = data.get('after')
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
