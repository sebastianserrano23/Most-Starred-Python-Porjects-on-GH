import requests

# make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers) # response stored in 'r' variable
print(f"Status code: {r.status_code}") # .status_code will let you know if the server is up (200 == good, 400/500 == bad)

# store API response in  variable
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# explore information about the repositories
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

print("\nSelected information about each repository:")
for first_repo in repo_dicts:
    print(f"Name: {first_repo['name']}")
    print(f"Owner: {first_repo['owner']['login']}")
    print(f"Stars: {first_repo['stargazers_count']}")
    print(f"Repository: {first_repo['html_url']}")
    print(f"created:L{first_repo['created_at']}")
    print(f"Updated: {first_repo['updated_at']}")
    print(f"Description: {first_repo['description']}")
