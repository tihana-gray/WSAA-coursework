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

fileContent = repoJSON["content"]
# Extracts the content of the file from the JSON response.
# 📚 Reference: https://docs.github.com/en/rest/repos/contents?apiVersion=2026-03-10#get-repository-content

decodedBytes = base64.b64decode(fileContent)
# Decodes the base64-encoded content of the file to get the original file content.
# 📚 References: https://docs.python.org/3/library/base64.html#base64.b64decode
# https://www.baeldung.com/java-base64-encode-and-decode

decodedContent = decodedBytes.decode("utf-8")
# Converts the decoded bytes into a string using UTF-8 encoding.
# 📚 References: https://docs.python.org/3/library/stdtypes.html#str.encode
# https://stackoverflow.com/questions/2941995/ignore-incorrect-padding-error-when-base64-decoding

print(decodedContent)

updatedContent = decodedContent.replace("Andrew", "Tihana")
# Replaces all occurrences of the name "Andrew" with "Tihana" in the decoded content.
# 📚 References: https://docs.python.org/3/library/stdtypes.html#str.replace
# https://www.w3schools.com/Jsref/jsref_replace.asp
# https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace

print(updatedContent)

encodedContent = base64.b64encode(updatedContent.encode("utf-8")).decode("utf-8")
# Encodes the updated content back into base64 format to prepare it for uploading to GitHub.
# 📚 References: https://docs.python.org/3/library/base64.html#base64.b64encode
# https://stackoverflow.com/questions/13110629/decoding-utf-8-strings-in-python

sha = repoJSON["sha"]
# Extracts the SHA of the file (required for updating the file).
# 📚 References: https://docs.github.com/en/rest/repos/contents?apiVersion=2026-03-10#update-a-file
# https://docs.gitlab.com/api/repositories/

data = {
    "message": "Replaced Andrew with Tihana",
    "content": encodedContent,
    "sha": sha
}
# Creating the data payload for updating the file on GitHub.
# 📚 Reference: https://docs.github.com/en/rest/repos/contents?apiVersion=2026-03-10#update-a-file

response = requests.put(url, json=data, auth=("token", apiKey))
# Sending a PUT request to update the file on GitHub.
# 📚 Reference: https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
# https://docs.github.com/en/rest/repos/contents?apiVersion=2026-03-10#update-a-file

print(response.status_code)