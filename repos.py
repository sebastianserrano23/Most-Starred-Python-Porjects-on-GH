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
print(f"Total repos: {response_dict['total_count']}") # 1

# explore information about the repos
repo_dicts = response_dict['items'] # 2 
print(f"Repos returned: {len(repo_dicts)}") 
# examine the first repo
repo_dict = repo_dicts[0] # 3
print(f"\nKeys: {len(repo_dict)}") # 4 
for key in sorted(repo_dict.keys()): # 5 
    print(key)


