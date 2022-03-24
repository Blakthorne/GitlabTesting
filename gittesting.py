from config import GITLAB_TOKEN
from git import Repo
import os, json, requests

# repo_path = os.getenv('C:\repos\sa\sa-web')
# repo = Repo(repo_path)
# currentBranch = "sermon-concept"
# git = repo.git

# commit = {
#     "branch": "sermon-concept",
#     "commit_message": "testing programmatic git",
#     "actions": [
#         {
#             "action": "update",
#             "file_path": "C:\repos\sa\sa-web\pages\broadcasters\_broadcaster.vue",
#             "content": "some content"
#         }
#     ]
# }

# json_commit = json.dumps(commit)

get_commit_info_url = "https://git.sermonaudio.com/api/v4/projects/105/repository/commits/d93a49cc224d69314e531862a2f174215df2647f"
get_commit_info_header = {"PRIVATE-TOKEN": GITLAB_TOKEN}
get_commit_info = requests.get(url = get_commit_info_url, headers = get_commit_info_header)

print(get_commit_info.json())

# def checkout(git):
#     git.checkout("-b", currentBranch)

# def add(git):
#     git.add("_broadcaster.vue")

# def commit(git):
#     git.commit("-m", "more broadcaster details")

# def push(git):
#     git.push("--set-upstream", "origin", currentBranch)

# checkout(git)
# add(git)
# commit(git)