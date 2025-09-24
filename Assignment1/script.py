from git import Repo

inputFile = open("./Input/VR_Project_List.txt")
lines = inputFile.readlines()

for line in lines:
    line = line.replace("\n", "")
    currentRepoPath = line
    currentRepoName = currentRepoPath.split(".git")[0].split('/')[-1]
    
    try:
        Repo.clone_from(currentRepoPath, f"./Repos/{currentRepoName}/")
        print(f"Cloned {currentRepoName}")
    except:
        print(f"{currentRepoName} Does not exist")
