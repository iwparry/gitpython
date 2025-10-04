from scripts import clone, commit, push

if __name__ == "__main__":
    cloning = input("Are you cloning a git repo? (Y/N): ").lower()
    if cloning == "y":
        print(f"Cloning repository")
        clone.run()
    else:
        print(f"Skipping clone")

    msg = input("Enter commit message: ").strip()
    if not msg:
        print("Commit message cannot be empty.")
        exit(1)

    commit.run(message=msg)
    push.run()

    print(f"Workflow ran successfully")