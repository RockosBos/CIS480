from git import Repo

currentRepoPath = "https://github.com/stefaanvermassen/virtual-museum-app.git"
currentRepoName = currentRepoPath.split(".git")[0].split('/')[-1]

Repo.clone_from(currentRepoPath, f"./Repos/{currentRepoName}/")
print("Repo Cloned")