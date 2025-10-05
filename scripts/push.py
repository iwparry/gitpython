from git import Repo

def git_push(origin="origin", branch="main"):
    push = origin.push(branch)
    return push

def run(path="./gitpython", origin="origin", branch="main"):
    repo = Repo(path)
    repo_origin = repo.remote(name=origin)
    git_push(repo_origin, branch)
    return f"Successfully pushed changes to {repo}"
    

if __name__ == "__main__":
    run()