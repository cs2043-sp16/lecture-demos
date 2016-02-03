# Forking a Repository

Today we will fork a repository!

## Step 1: Fork it!

Click on the Fork in the top right of the screen, follow the on screen prompts.

## Where does it access files from?

We are going to follow the directions from [GitHub](https://help.github.com/articles/configuring-a-remote-for-a-fork/), inlined here for convenience:

### Open Terminal (for Mac and Linux users) or the command prompt (for Windows users).

### List the current configured remote repository for your fork.

```
git remote -v
origin  https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
origin  https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)
```

### Specify a new remote upstream repository that will be synced with the fork.

```
git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git
```

So we actually need to set it to be `https://github.com/cs2043-sp16/lecture-demos.git`.

### Verify the new upstream repository you've specified for your fork.

```
git remote -v
origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)
upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (fetch)
upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (push)
```

## Step 2: Let's See if it Worked (files are added...)

Uploading this file right now!

## Step 3: Sync your Fork

Again, straight from [GitHub](https://help.github.com/articles/syncing-a-fork/).

