from git import Repo

inputFile = open("./Input/VR_Project_List.txt")
lines = inputFile.readlines()

print(lines[3])

currentRepoPath = "https://github.com/stefaanvermassen/virtual-museum-app.git"
currentRepoName = currentRepoPath.split(".git")[0].split('/')[-1]

Repo.clone_from(currentRepoPath, f"./Repos/{currentRepoName}/")
print("Repo Cloned")