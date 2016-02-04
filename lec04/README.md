# Forking a Repository

Today we will fork a repository!  Video at the bottom of me doing it step by step.

## Step 1: Fork it!

Click on the Fork in the top right of the screen, follow the on screen prompts.

## Where does it access files from?

We are going to follow the directions from [GitHub](https://help.github.com/articles/configuring-a-remote-for-a-fork/), inlined here for convenience:

1. Open Terminal (for Mac and Linux users) or the command prompt (for Windows users).

2. List the current configured remote repository for your fork.

    ```
    git remote -v
    origin  https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
    origin  https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)
    ```

3. Specify a new remote upstream repository that will be synced with the fork.

    ```
    git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git
    ```

    So we actually need to set it to be `https://github.com/cs2043-sp16/lecture-demos.git`.

4. Verify the new upstream repository you've specified for your fork.

    ```
    git remote -v
    origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
    origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)
    upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (fetch)
    upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (push)
    ```

## Step 2: Let's See if it Worked (files are added...)

Uploading this file right now!  (If you are following this after the lecture, you will only be able to sync your fork when new files are added).

## Step 3: Sync your Fork

Again, straight from [GitHub](https://help.github.com/articles/syncing-a-fork/), inlined here for convenience.

1. Open Terminal (for Mac and Linux users) or the command prompt (for Windows users).

2. Change the current working directory to your local project.

3. Fetch the branches and their respective commits from the upstream repository. Commits to master will be stored in a local branch, upstream/master.

    ```
    git fetch upstream
    remote: Counting objects: 75, done.
    remote: Compressing objects: 100% (53/53), done.
    remote: Total 62 (delta 27), reused 44 (delta 9)
    Unpacking objects: 100% (62/62), done.
    From https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY
     * [new branch]      master     -> upstream/master
    ```

4. Check out your fork's local master branch.

    ```
    git checkout master
    Switched to branch 'master'
    ```

5. Merge the changes from upstream/master into your local master branch. This brings your fork's master branch into sync with the upstream repository, without losing your local changes.

    ```
    git merge upstream/master
    Updating a422352..5fdff0f
    Fast-forward
     README                    |    9 -------
     README.md                 |    7 ++++++
     2 files changed, 7 insertions(+), 9 deletions(-)
     delete mode 100644 README
     create mode 100644 README.md
     ```

    If your local branch didn't have any unique commits, Git will instead perform a "fast-forward":

    ```
    git merge upstream/master
    Updating 34e91da..16c56ad
    Fast-forward
     README.md                 |    5 +++--
     1 file changed, 3 insertions(+), 2 deletions(-)
   ```

# Step by step screen capture

The process from start to finish, with a little extra.  ~15min of your time, if you are following along.

## 1. <a href="https://youtu.be/RQrDsLk4rZs" target="_blank">Setup the remote</a>

## 2. <a href="https://youtu.be/ZnSFmYstgaA" target="_blank">Sync with the remote when there are changes</a>
