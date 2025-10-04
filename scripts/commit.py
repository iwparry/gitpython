from git import Repo

def git_add(repo):
    add = repo.git.add(A=True) # git add .
    return add

def git_commit(repo, msg):
    commit = repo.index.commit(msg) # git commit -m "msg"
    return commit

if __name__ == "__main__":
    git_repo = Repo("./gitpython")
    # message = "First commit via GitPython"
    message = "Fix push.py script - missin () for origin.push()"

    git_add(git_repo)
    git_commit(git_repo, message)

    print(f"Change successfully committed, commit message: {message}")