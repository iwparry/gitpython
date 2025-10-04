from git import Repo

def git_push(origin):
    push = origin.push()
    return push

if __name__ == "__main__":
    git_repo = Repo("./gitpython")
    git_origin = git_repo.remote(name="origin")

    git_push(git_origin)

    print(f"Successfully pushed changes to {git_repo}.")