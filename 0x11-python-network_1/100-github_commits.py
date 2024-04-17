#!/usr/bin/python3
"""
Python script that lists 10 commits (from the most recent to oldest) of
a given repository by a specified user.
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner_name, repo_name)
    response = requests.get(url)
    commits = response.json()
    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print("{}: {}".format(sha, author_name))
