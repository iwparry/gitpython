from git import Repo

def git_push(origin):
    push = origin.push()
    return push

def run(path="./gitpython", origin="origin"):
    repo = Repo(path)
    repo_origin = repo.remote(name=origin)
    git_push(repo_origin)
    return f"Successfully pushed changes to {repo}"
    

if __name__ == "__main__":
    run()