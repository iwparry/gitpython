from git import Repo

def git_add(repo):
    add = repo.git.add(A=True) # git add .
    return add

def git_commit(repo, msg):
    commit = repo.index.commit(msg) # git commit -m "msg"
    return commit

def run(path="./gitpython", message="GitPython commit"):
    """Add + commit changes for a given repo path."""
    repo = Repo(path)
    git_add(repo)
    git_commit(repo, message)
    return f"✅ Change successfully committed, commit message: {message}"

if __name__ == "__main__":
    run()