from urllib import response
import requests 

# make an API call and store the respone
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' 
headers = {'Accept': 'application/vnd.github.v3+json'} 
r = requests.get(url, headers=headers) 
print(f'Status code: {r.status_code}') 
print(r)

# Store API response in a variable 
response_dict = r.json() 
print(f"Total repos: {response_dict['total_count']}")

# explore information about the repos
repo_dicts = response_dict['items'] 
print(f"Repos returned: {len(repo_dicts)}") 

print(f"\nSelected information about each repository:")

for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}") 
    print(f"Owner: {repo_dict['owner']['login']}") 
    print(f"Stars: {repo_dict['stargazers_count']}") 
    print(f"Repos: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}") 
    print(f"Updated: {repo_dict['updated_at']}") 
    print(f"Description: {repo_dict['description']}")

