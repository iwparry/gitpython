import os
import git

def git_clone(url, dir):
    if os.path.exists(dir) and os.path.isdir(os.path.join(dir, ".git")):
        print(f"Repository already exists at '{dir}', skipping clone.")
        return git.Repo(dir)
    clone = git.Repo.clone_from(url, dir)
    return clone

def run(url="https://github.com/iwparry/gitpython.git", dir="gitpython"):
    git_clone(url, dir)
    return f"{url} successfully cloned to {dir}"

if __name__ == "__main__":
    run()