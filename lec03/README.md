# Ownership exercise

I have created the file `gen_demo.sh` that will create some files for you to play around with modifying the permissions on.

Since we are experimenting with file permissions, you will need to execute this exercise as the root user.  However, it is best for you to first examine what things look like as a regular user!

## Step 1: <a href="https://en.wikipedia.org/wiki/Exogenesis:_Symphony" target="_blank">Exogenesis</a>

The `gen_demo.sh` script is currently not executable.

1. Make `gen_demo.sh` an executable file.
2. Executing `gen_demo.sh` as a regular user will intentionally fail.  Instead, you will need to execute it as the root user.

```
>>> sudo ./gen_demo.sh
```

You now have some files generated for you to experiment with.  Please do **not** become root first, as you will miss out on part of the experience.  As in do not do the following:

```
>>> sudo su      # or just >>> su
>>> ./gen_demo.sh
```

For the purposes of this exercise, *do not* look inside `gen_demo.sh`.  It'll spoil the fun, and there really isn't anything for you there.

## Step 2: Inspection

You now have a `demo` folder, which has one subdirectory and a file inside of the subdirectory.  First, lets list the directory recursively to see everything inside:

```
>>> ls -R demo/
```

We have learned a little bit about the contents of demo now, but the file in the subdirectory is rather ominous...maybe we can glean more information by passing the `-a` flag to `ls`?  I will also use the `-l` format because I prefer to view things in list format.

```
>>> ls -alR demo/
```

Woah!  Maybe aliens really did hack your computer.  Doesn't matter, we're smarter than them.

## Step 3: Gain access

Noting that you should be careful not to execute any form of `rm` command, become the root user.

```
>>> sudo su
```

or just

```
>>> su
```

if you know the root password (it started as `root` on the course VMs).

Your first manipulation task is to fix the permissions on the `lemmings` directory.  Refer back to the lecture slides to determine how to do this, as well as how to discover what they should be.

- *Hint*: The top-level `demo` directory has the correct permissions.
- *Note*: These are what *almost all* directory permissions should be, but not always

## Step 4: Find the lemmings

Change the permissions such that you are able to execute

```
>>> cat demo/lemmings/are_watching_you.txt
```

Go ahead and try that first.  Even as root, you have been denied.

1. Change the permissions so that only the root user can `cat` the file.

   Verify your success of only permitting the root user by exiting and catting it again as the regular user:

   ```
   >>> exit
   >>> cat demo/lemmings/are_watching_you.txt
   ```

2. Become the super user again.  Now change the permissions so that you can warn your regular users where these little guys are.  Verify your success again.

## Step 5: Become the leader

As we all know, lemmings will pretty much do anything (including running off cliffs if all the other lemmings are).  Lets go ahead and move them up one directory.

1. Change the **ownership** of the entire `demo` directory tree to a non-root user (e.g. on the course vm change it to `student`).
    - Not on the VM?  Execute `users` to find one
2. Change the **group** of the entire `demo` directory tree to a non-root user.
    - Not on the VM?  Execute `groups <user_from_1>` to see which groups this user is a part of
    - **EXCEPT**: do not change it to `wheel`.  We may cover `wheel` later in the course if there is time.  Just don't use it ;)

- *Hint*: you can execute (1) and (2) with one `chown` command.

Become your regular user again.  You should be able to `ls -alR` to see whether you were successful or not.  Now move the lemmings so that the directory structure is

```
- demo/
    - lemmings/
    - are_watching_you.txt
```

instead of

```
- demo/
    - lemmings/
        - are_watching_you.txt
```