# GitPython

## Introduction
GitPython is a Python library used to interact with Git repositories.

For more information check the [official documentation](https://gitpython.readthedocs.io/en/stable/) or visit the [GitHub repository](https://github.com/gitpython-developers/GitPython).

This is my own repository where I simply play around with the tool since I've developed an interest in it. Basically at work I have a task I need to complete that involves making the same change in the numerous repositories that myself and my team manages. 
As anyone could imagine going through each repository one by one, branching off from main, making the change, then having to commit and push those changes, over and over in a lot of repositories is a tedious activity. 

So like anyone else would in my position I want to write a script that takes care of all this for me. In my case I'm quite partial to using Python as my language of choice when it comes to writing scripts, I was already aware that I could achieve what I want by making use of other libraries like `os`, `subprocess` for example, but I only came across `GitPython` quite recently so thought I might as well try to make use of something more specific to my case.

__At the time of writing: everything to this point was written directly in GitHub, this repository wasn't initialised locally and hasn't yet been cloned as I intend to do this via GitPython__

I was able to successfully clone the repository using the following script:

```python
import git

git_url = "https://github.com/iwparry/gitpython.git"

def git_clone(url):
    clone = git.Repo.clone_from(url, 'gitpython')
    return clone

if __name__ == "__main__":
    git_clone(git_url)
```

So we import the library, `git`, I saved my git repository url to a variable and created a function called `git_clone`, that accepts a git repo url as an argument, to execute the clone.

Inside my function I created a variable `clone` and assigned to this variable is what cloned my repository, `git.Repo.clone_from(url, 'gitpython)` here it accepts two arguments, the first being the url of the git repository we wish to clone, the second is the local path in which the repository needs to be created, e.g. when you clone via the command line `git clone {url}` a new directory will be created in the current working directory under the name of the git repository by default but in this case you'll need to specify the name of the directory.

__Everything from line 15 onwards in this file has been written locally, the following will demonstrate how to we add, commit, and push changes to our remote git repository.__

I have successfully pushed to `main` using the scripts saved in `scripts/`, `commit.py` and `push.py`

__FIX: The original script `push.py` that was committed was missing `()` - fixing in latest commit to `main`__

Since I've edited this script last I've written up a `main.py` script that executes all the modular scripts in the `scrips/` directory, no now I have a single script to handle the workflow `clone -> commit -> push` and have included user prompts for whether we want to clone a repo and to provide a commit message. 

Example:
```
$ gitpython/main.py
Are you cloning a git repo? (Y/N): Y
Cloning repository
Repository already exists at 'gitpython', skipping clone.
Enter commit message: Updating README.md
Workflow ran successfully
```
Will be utilising `argparse` to run the script with flags rather than needing to prompt the user for values.

Have now added the following argparse arguments to the script with the only required argument being `--message`

```
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
    args = parser.parse_args()
```
So now I simply run:
```
python gitpython/main.py --clone True --message "Update README.md with argparse entries"
Cloning repository
Repository already exists at './gitpython', skipping clone.
Workflow ran successfully
```