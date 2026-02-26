import requests
import json
from config import config as cfg

username = "tihana-gray"

# repo name you chose
repo = "private_repo"

url = f"https://api.github.com/repos/{username}/{repo}"

apiKey = cfg["githubkey"]   # read token from config.py

# GitHub API authentication
response = requests.get(url, auth=('token', apiKey))

repoJSON = response.json()

# write result to file
with open("repo_output.json", "w") as fp:
    json.dump(repoJSON, fp, indent=4)

print("Done. Check repo_output.json")