from github import Github
from config import config as cfg

apikey = cfg["githubkey"]
g = Github(apikey)

# simple test: list repos on your GitHub account
for repo in g.get_user().get_repos():
    print(repo.name)