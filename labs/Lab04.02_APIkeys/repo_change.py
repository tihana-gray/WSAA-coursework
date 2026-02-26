import requests
import base64
import json
from config import config as cfg

username = "tihana-gray"
repo = "private_repo"

apiKey = cfg["githubkey"]

# File we want to update in the repo
path = "api_test.txt"

# New content for the file
new_content = "This file was updated using the GitHub API.\n"
encoded = base64.b64encode(new_content.encode()).decode()

# First: get file info (to check if it exists)
get_url = f"https://api.github.com/repos/{username}/{repo}/contents/{path}"
get_response = requests.get(get_url, auth=('token', apiKey))

if get_response.status_code == 200:
    sha = get_response.json()['sha']
else:
    sha = None  # File does not exist yet

# Prepare update request
put_url = get_url
payload = {
    "message": "API update to api_test.txt",
    "content": encoded
}

if sha:
    payload["sha"] = sha  # required if updating existing file

response = requests.put(put_url, auth=('token', apiKey), json=payload)

print("Status:", response.status_code)
print("Result written to update_output.json")

with open("update_output.json", "w") as fp:
    json.dump(response.json(), fp, indent=4)