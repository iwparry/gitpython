from git import Repo

def git_merge(repo, source):
    merge = repo.git.merge(source)
    return merge

def run(path="./gitpython", source="main"):
    repo = Repo(path)
    git_merge(repo, source)
    return f"Successfully merged changes from {source}"

if __name__ == "__main__":
    run()