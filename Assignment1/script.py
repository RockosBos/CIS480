from git import Repo

print("Would you like to Clone Repos (Y/N)?")
cloneRepoInput = input()

inputFile = open("./Input/VR_Project_List_short.txt")
lines = inputFile.readlines()

if(cloneRepoInput == "Y" or cloneRepoInput == "y"):

    print(f"Cloning {len(lines)} Repositories")
    for line in lines:
        line = line.replace("\n", "")
        currentRepoURL = line
        currentRepoName = currentRepoURL.split(".git")[0].split('/')[-1]
        print(f"Cloning {currentRepoName}...")
        try:
            Repo.clone_from(currentRepoURL, f"./Repos/{currentRepoName}/")
            print(f"Cloned {currentRepoName} Successfully")
        except:
            print(f"Error Cloning {currentRepoName}")

print("Analyzing Repositories")

for line in lines:
    line = line.replace("\n", "")
    currentRepoURL = line
    currentRepoPath = f"./Repos/{currentRepoURL.split('.git')[0].split('/')[-1]}"

    print(currentRepoPath)
    try:
        currentRepoLocal = Repo(f"{currentRepoPath}/")
        print(currentRepoLocal.commit('master'))
    except:
        print(f"Failed to open repo")
