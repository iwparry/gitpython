import git

def git_clone(url, dir):
    clone = git.Repo.clone_from(url, dir)
    return clone

if __name__ == "__main__":
    git_url = "https://github.com/iwparry/gitpython.git"
    git_dir = "gitpython"

    git_clone(git_url, git_dir)
    print(f"Git clone of {git_url} to {git_dir} successful.")