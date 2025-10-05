import argparse
from scripts import clone, commit, push, branch, merge

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--clone",
        type=bool,
        default=False
    )
    parser.add_argument(
        "--git-url",
        type=str,
        default="https://github.com/iwparry/gitpython.git"
    )
    parser.add_argument(
        "--git-dir",
        type=str,
        default="./gitpython"
    )
    parser.add_argument(
        "--message",
        type=str,
        required=True
    )
    parser.add_argument(
        "--branch",
        type=str,
        default="main"
    )
    parser.add_argument(
        "--merge",
        type=bool,
        default=False
    )
    parser.add_argument(
        "--source",
        type=str,
        default="main"
    )
    args = parser.parse_args()

    if args.clone:
        print(f"Cloning repository")
        clone.run(url=args.git_url, dir=args.git_dir)
    else:
        print(f"Skipping clone")
    if args.merge:
        print(f"merge argument provided - merging {args.source} to current")
        print(f"Fist, commit and push unsaved changes")
        commit.run(message=args.message)
        merge.run(source=args.source)
        
    if args.branch:
        print(f"Branch argument provided - running branch workflow")
        branch.run(branch=args.branch)
        commit.run(message=args.message)
        push.run(branch=args.branch)

    print(f"Workflow ran successfully")