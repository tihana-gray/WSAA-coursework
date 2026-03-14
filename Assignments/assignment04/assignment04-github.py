import requests
import base64
from config import config as cfg


apiKey = cfg["githubkey"]
# Retrieving the GitHub API key from the config.py file
# 📚 References: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# https://gist.github.com/win3zz/0a1c70589fcbea64dba4588b93095855

owner = "tihana-gray"
# My repo username
# 📚 Reference: https://docs.github.com/en/rest

repo = "WSAA-coursework"
# Repository name where the file exists
# 📚 Reference: https://docs.github.com/en/rest/repos/contents?apiVersion=2026-03-10#get-repository-content

path = "Assignments/assignment04/andrew_story.txt"
# Path to the file in the repository that we want to update
# 📚 Reference: https://docs.github.com/en/rest/repos/contents?apiVersion=2026-03-10#update-a-file

url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
# This URL is used to access the contents of the specified file in the GitHub repository.
# 📚 Reference: https://docs.github.com/en/rest/repos/contents?apiVersion=2026-03-10

response = requests.get(url, auth=("token", apiKey))
# This line sends an HTTP GET request to the specified URL with authentication using the API key.
# 📚 Reference: https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request

repoJSON = response.json()
# Converts the JSON response from the API into a Python dictionary.
# 📚 Reference: https://requests.readthedocs.io/en/latest/user/quickstart/#json-response-content

print(response.status_code)

repoJSON = response.json()