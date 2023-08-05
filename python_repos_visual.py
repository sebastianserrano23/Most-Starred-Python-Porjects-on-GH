from fileinput import filename
import requests

from plotly.graph_objs import Bar
from plotly import offline

# make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers) # response stored in 'r' variable
print(f"Status code: {r.status_code}") # .status_code will let you know if the server is up (200 == good, 400/500 == bad)

# Process results
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars = [], []

for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# make Visualization
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars
}]

my_layout = {
    'title': 'Most-Starred Python Porjects on Github',
    'x-axis': {'title': 'Repository'},
    'y-axis': {'title': 'Stars'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')