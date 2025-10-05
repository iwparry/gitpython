from git import Repo

def list_branches(repo):
    branch_list = []
    for branch in repo.branches:
        branch_list.append(branch.name)
    return branch_list

def create(name, repo):
    print(f"Creating new branch {name}")
    new_branch = repo.create_head(name)
    return new_branch

def checkout(name, repo):
    print(f"Checkout to branch: {name}")
    checkout = repo.git.checkout(name)
    return checkout

def run(branch="main", path="./gitpython"):
    repo = Repo(path)
    branches = list_branches(repo)
    if branch.strip() == str(repo.active_branch):
        print(f"Nothing to do, {branch} is already the active branch.")
    elif branch.strip() in branches:
        print(f"Branch already exists, changing branch to {branch}")
        checkout(branch, repo)
    else:
        print(f"Branch, {branch} doesn't exist, creating branch.")
        create(branch, repo)
        print(f"Changing to new branch, {branch}")
        checkout(branch, repo)


if __name__ == "__main__":
    run()
