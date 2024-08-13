#!/usr/bin/python3
"""
By Ab Yahaya
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If the subreddit is invalid or there is an error, the function returns 0.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            try:
                data = response.json()
                subscribers = data.get('data', {}).get('subscribers', 0)
                return subscribers
            except ValueError:
                # Handle the case where the response is not JSON
                print("Error: Response is not valid JSON.")
                return 0
        else:
            # Handle non-200 status codes
            print(f"Error: Received status code {response.status_code}")
            return 0
    except requests.RequestException as e:
        # Handle any network-related errors
        print(f"Error: Request failed - {e}")
        return 0
