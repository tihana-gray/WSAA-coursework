from github import Github
from config import config as cfg
import requests

apikey = cfg["githubkey"]
g = Github(apikey)

repo = g.get_repo("tihana-gray/private_repo")   
print("Clone URL:", repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
print("Download URL:", urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
print("Original contents:\n", contentOfFile)

newContents = contentOfFile + "more stuff\n"
print("New contents:\n", newContents)

updateResponse = repo.update_file(
    fileInfo.path,
    "updated by prog",
    newContents,
    fileInfo.sha
)

print("Update complete:")
print(updateResponse)