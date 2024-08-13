#!/usr/bin/python3
"""
AB Yahaya
"""
from collections import defaultdict
import re
import requests


def count_words(subreddit, word_list, hot_list=[], after=None, word_count=defaultdict(int)):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        hot_list (list): Accumulator for titles of hot articles.
        after (str): The 'after' parameter for pagination.
        word_count (dict): Dictionary to store the count of keywords.

    Returns:
        None: Prints the sorted count of keywords.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
        'User-Agent': 'python-requests/2.28.1'
    }
    params = {'after': after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            children = data.get('children', [])
            if not children and not hot_list:
                return None  # No posts found for the subreddit
            
            for child in children:
                title = child['data']['title'].lower()  # Convert title to lowercase
                hot_list.append(title)
                # Count occurrences of each word in the title
                for word in word_list:
                    if re.search(rf'\b{word.lower()}\b', title):
                        word_count[word.lower()] += title.split().count(word.lower())
            
            after = data.get('after')
            if after:
                return count_words(subreddit, word_list, hot_list, after, word_count)
            else:
                # Sort word_count by count (descending) and alphabetically for ties
                sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_word_count:
                    if count > 0:
                        print(f"{word}: {count}")
        else:
            return None
    except requests.RequestException:
        return None
