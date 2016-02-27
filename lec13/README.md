# Creating your own branch

In this exercise your boss has given you a random number generator with some various examples of how you can write python2 and python3 code in one file.  They want you to be able to export to a csv as well as the current format, which just separates it with spaces.

You explain to your boss that it makes more sense to have this functionality on a separate branch to make life easier.

## First: work locally

Now that you have synced up your fork and have `lec13/gen_numbers.py` on your computer, you'll want to make a new local branch.  We can verify what branch we are on with `git branch -a`:

```bash
>>> git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
  remotes/upstream/master
```

The above shows us that we are currently on the `master` branch (indicated by the `*`), and that we also have pointers to some remote branches: the `upstream/master` branch where you have been pulling updates from, and the `origin/master` branch where you have been able to push your changes to various exercises to.

### Make a new local branch

To do this, we can take a shortcut and give the `-b` flag to both create and checkout a branch at the same time:

```bash
>>> git checkout -b lec13_csv
Switched to a new branch 'lec13_csv'
```

We can verify that we are on this new local branch the same way as before:

```bash
>>> git branch -a
* lec13_csv
  master
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
  remotes/upstream/master
```

## Second: make your changes

Now that you are on a new branch, you can implement the alternate functionality your boss has asked for.

There are two lines you need to change:

1. The file you are generating is now a csv, so the file extension should be changed:

    ```py
    FILE_NAME="numbers.txt"
    ```
  
    on line 32 should become
    
    ```py
    FILE_NAME="numbers.csv"
    ```
    
2. The writing to the file should change from being separated by spaces to separated by commas:

    ```py
    f.write("%d " % next_int)
    ```
    
    on line 39 should change to
    
    ```py
    f.write("%d," % next_int)
    ```
    
    Yes...this will give us an extra comma at the end of the line.  You are welcome to fix the implementation (you just need to check if this is the last number to write to the row), but that is not the point of the exercise.
    
### Verify that you have made your changes

If you run the script with `python gen_numbers.py`, it should now create a `csv` instead of a `txt`.  You can also use `git status` or `git difftool` to see what has changed.

## Third: commit and push

We are now ready to put our changes online!  We will need to commit our changes:

```bash
>>> git commit -am "adding csv functionality on a separate branch for convenience"
```

However, when I run

```bash
>>> git push

fatal: The current branch lec13_csv has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin lec13_csv
```

what `git` is telling me is that the current **local** branch that we are working on does not currently have a location on the remote server (GitHub in our case) to push to.  Conveniently, it tells us exactly what we need to do:

```bash
>> git push --set-upstream origin lec13_csv
Counting objects: 4, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 376 bytes | 0 bytes/s, done.
Total 4 (delta 2), reused 0 (delta 0)
To https://github.com/sjm324/lecture-demos.git
 * [new branch]      lec13_csv -> lec13_csv
Branch lec13_csv set up to track remote branch lec13_csv from origin.
```

As you can see at the end, it has made a new branch on the remote server and the current local branch will track from there as well.  We can further verify:

```bash
>>> git branch -a
* lec13_csv
  master
  remotes/origin/HEAD -> origin/master
  remotes/origin/lec13_csv <--------- NEW BRANCH ON REMOTE!!!
  remotes/origin/master
  remotes/upstream/master
```

recalling that when we do

```bash
>>> git remote -v
origin	https://github.com/sjm324/lecture-demos.git (fetch)
origin	https://github.com/sjm324/lecture-demos.git (push)
upstream	https://github.com/cs2043-sp16/lecture-demos.git (fetch)
upstream	https://github.com/cs2043-sp16/lecture-demos.git (push)
```

it makes sense now that our new branch shows up under `origin/lec13_csv` since that is our personal `lecture-demos` repository.  If I had another branch on the course `lecture-demos` repository then you would be able to access it from `upstream/<branch_name>`.

## Switch back to master, just because you can

So now if we do

```bash
>>> git checkout master
Switched to branch 'master'
Your branch is up-to-date with 'origin/master'.
```

we will have the original code back, and can verify once again where we are:

```bash
>>> git branch -a
  lec13_csv
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/lec13_csv
  remotes/origin/master
  remotes/upstream/master
```

If we run `python gen_numbers.py` now, it will create the `txt` file instead of a `csv`.

## Comparing across branches

As we talked about in previous lectures, we can compare code across branches very easily!  Just run `git difftool` with the two branches you want to compare.

```bash
>>> git difftool master lec13_csv
```

Since we had `master` as the first argument and `lec13_csv` as the second argument, it will show the `master` code on the left and the `lec13_csv` code on the right.

## In the end

We have now talked about branching quite a bit.  When to create a new branch and when to add in some `if` statements to your code and let the user specify things depend greatly on the nature of the program you are writing.  In a real-world scenario if my boss had told me to enable exporting to a `csv` instead, I would have just made that be an argument the user could specify.

But this is a nice little example just to show that you can share code across different branches and have mostly the same code-base, but produce a different output / behavior.
