from scripts import commit, push

if __name__ == "__main__":
    msg = input("Enter commit message: ").strip()
    if not msg:
        print("Commit message cannot be empty.")
        exit(1)

    commit.run(message=msg)
    push.run()

    print(f"Workflow ran successfully")