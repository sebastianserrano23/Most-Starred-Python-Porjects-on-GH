from email import header
from http.client import responses
import re
from urllib import request, response
import requests

# make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status: {r.status_code}')

# store API response in a variable
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# examine the first repository
first_repo = repo_dicts[0]
print(f"\nKeys: {len(first_repo)}")
for key in sorted(first_repo.keys()):
    print(key)