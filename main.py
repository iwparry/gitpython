from scripts import commit, push

if __name__ == "__main__":
    msg = "Centralize script for git add, commit and push"

    commit.run(message=msg)
    push.run()