import requests
import json
from config import config as cfg

username = "tihana-gray"
repo = "private_repo"

url = f"https://api.github.com/repos/{username}/{repo}/commits"

apiKey = cfg["githubkey"]

response = requests.get(url, auth=('token', apiKey))
data = response.json()

with open("repo_commits.json", "w") as fp:
    json.dump(data, fp, indent=4)

print("Commit data saved to repo_commits.json")