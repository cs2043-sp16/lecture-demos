# Ownership solution

These are the steps to complete the assignment.  There are many ways to complete it, these are just one possible way.  This demo was a little *too* long / involved, sorry!  I was having a little too much fun with the strange permissions...

## Step 1: Exogenesis

1. To make `gen_demo.sh` executable, we need to modify the permissions.  Assuming you are in this directory (aka if you do `ls` and see `gen_demo.sh`), then let's first check what the permissions currently are:

    ```
    >>> ls -al gen_demo.sh
    -rw-rw-r--. 1 sven sven 2.6K Feb  4 12:16 gen_demo.sh
    ```
    This indicates that nobody can run this file as an executable.  To change this, we do

    ```
    >>> chmod a+x gen_demo.sh
    ```

    will make it executable for all users.  The script forces that you run it as root anyway, so the difference between `a`, `g`, and `o` in this context is insignificant.

    To confirm, let's look at the permissons again

    ```
    >>> ls -al gen_demo.sh
    -rwxrwxr-x. 1 sven sven 2.6K Feb  4 12:16 gen_demo.sh*
    ```

    Yours may or may not have the `*` after it, but we can see now that all users now have the `x` flag set.

2. Now that the script is executable, if we run it we will get the demo.

    As a side note, if we run it as a regular user we will get the message

    ```
    >>> ./gen_demo.sh
    You must execute this script as the root user...
    ...try typing this:

        sudo gen_demo.sh
    ```

    So lets go ahead and run the script as the super user.  This is done because we are doing an exercise with permissions, which only the `root` can do all of the steps remaining.

    ```
    >>> sudo ./gen_demo.sh
    [sudo] password for student:
    Your playground has been constructed!  Follow the directions in the README.
    ```

    If I run `ls` now, I will see that a new folder called `demo` has been created.

## Step 2: Inspection

When I follow the directions as a regular user, I will get

```
>>> ls -R demo/
demo/:
lemmings/

demo/lemmings:
ls: cannot access demo/lemmings/are_watching_you.txt: Permission denied
are_watching_you.txt
```
and similarly
```
>>> ls -alR demo/
demo/:
total 12K
drwxrwxr-x. 3 root root 4.0K Feb  4 12:23 ./
drwxrwxr-x. 3 sven sven 4.0K Feb  4 12:23 ../
dr--r--r--. 2 root root 4.0K Feb  4 12:23 lemmings/

demo/lemmings:
ls: cannot access demo/lemmings/are_watching_you.txt: Permission denied
ls: cannot access demo/lemmings/..: Permission denied
ls: cannot access demo/lemmings/.: Permission denied
total 0
d????????? ? ? ? ?            ? ./
d????????? ? ? ? ?            ? ../
-????????? ? ? ? ?            ? are_watching_you.txt
```

If you see something else, this is because you were still the `root` user because you did `su` followed by `./gen_dem.sh` instead of `sudo ./gen_demo.sh`.  You can execute the command `whoami` and any time to confirm who you are.  You may also have seen something differnet on Mac.  If you executed the above as `root`, then you would have seen

```
>>> ls -R demo/
demo/:
lemmings/

demo/lemmings:
are_watching_you.txt
```

followed by

```
>>> ls -alR demo/
demo/:
total 12K
drwxrwxr-x. 3 root root 4.0K Feb  4 12:23 ./
drwxrwxr-x. 3 sven sven 4.0K Feb  4 12:23 ../
dr--r--r--. 2 root root 4.0K Feb  4 12:23 lemmings/

demo/lemmings:
total 12K
dr--r--r--. 2 root root 4.0K Feb  4 12:23 ./
drwxrwxr-x. 3 root root 4.0K Feb  4 12:23 ../
----------. 1 root root   15 Feb  4 12:23 are_watching_you.txt
```

## Step 3: Gain access

#### Discover the correct permissions to use:

<table>
<th>Linux</th> <th>Mac</th>
<tr>
<td>
<pre>
>>> stat --format %a demo/
775
</pre>
</td>
<td>
<pre>
>>> stat -f %A demo/
775
</pre>
</td>
</table>

Just because we can, let's see what the octal format of the permissions are of the `lemmings` directory:

<table>
<th>Linux</th> <th>Mac</th>
<tr>
<td>
<pre>
>>> stat --format %a demo/lemmings/
444
</pre>
</td>
<td>
<pre>
>>> stat -f %A demo/lemmings/
444
</pre>
</td>
</table>

#### Change the permissions of the `lemmings` directory

Now that we know what they should be, lets change them using `chmod`.  We will need to become the root user first.

```
>>> sudo su
[sudo] password for student:
>>> whoami
root
>>> chmod 755 demo/lemmings/
```

You could also have just executed `sudo chmod 755 demo/lemmings/`, but I want to give you more practice becoming root and leaving that state as well.

## Step 4: Find the lemmings

So at this point we are the `root` user, and some of you may have been following along and been confused because the following sequence gave

```
>>> cat demo/lemmings/are_watching_you.txt
from behind!!!
```

This is because you are still the `root` and can do pretty much whatever you want...if we do

```
>>> exit
exit
>>> whoami
student
>>> cat demo/lemmings/are_watching_you.txt
cat: demo/lemmings/are_watching_you.txt: Permission denied
```

we can see that normal users still cannot find out where those pesky lemmings are.  However, now we can discover what the permissions are since we have fixed the directory permissions for `demo/lemmings`:

```
>>> ls -al demo/lemmings/are_watching_you.txt
----------. 1 root root 15 Feb  4 12:23 demo/lemmings/are_watching_you.txt
```

We only want to let our users read this file, so I can execute

```
>>> sudo chmod ugo+r demo/lemmings/are_watching_you.txt
[sudo] password for student:
>>> ls -al demo/lemmings/are_watching_you.txt
-r--r--r--. 1 root root 15 Feb  4 12:23 demo/lemmings/are_watching_you.txt
>>> whoami
student
>>> cat demo/lemmings/are_watching_you.txt
from behind!!!
```

Note that `chmod ugo+r` is the same as `chmod a+r`, but may as well try different things.

## Step 5: Become the leader

Right now we can see that `root` owns everything inside of the `demo` folder, as well as the `demo` folder itself:

```
>>> ls -lR demo/
demo/:
total 4.0K
drwxr-xr-x. 2 root root 4.0K Feb  4 12:23 lemmings/

demo/lemmings:
total 4.0K
-r--r--r--. 1 root root 15 Feb  4 12:23 are_watching_you.txt
```

That is, `root` is both the owner as well as the group is `root` as well.  Which means that right now if we try and move the text file

```
>>> mv demo/lemmings/are_watching_you.txt demo/
mv: cannot move `demo/lemmings/are_watching_you.txt` to `demo/are_watching_you.txt`: Permission denied
```

we will not succeed.  Recalling that we could use `chown` to change the ownership, and then use `chgrp` to change the group of the files independently, we can also do this in one fowl swoop combining recursion and the less common `chown user:group` syntax:

```
>>> sudo chown -R student:student demo/
>>> ls -lR demo/
demo/:
total 4.0K
drwxr-xr-x. 2 student student 4.0K Feb  4 12:23 lemmings/

demo/lemmings:
total 4.0K
-r--r--r--. 1 sven sven 15 Feb  4 12:23 are_watching_you.txt
> mv demo/lemmings/are_watching_you.txt demo/
> ls -lR demo/
demo/:
total 8.0K
-r--r--r--. 1 student student   15 Feb  4 12:23 are_watching_you.txt
drwxr-xr-x. 2 student student 4.0K Feb  4 14:10 lemmings/

demo/lemmings:
total 0
```

**Note**: On mac you usually are not allowed to assign the group to your username unless you have specifically set that up.  To see what groups are available, execute the `groups` command to see what the options are:

```
>>> groups
staff com.apple.sharepoint.group.2 everyone localaccounts _appserverusr admin _appserveradm _lpadmin com.apple.sharepoint.group.1 _appstore _lpoperator _developer com.apple.access_ftp com.apple.access_screensharing com.apple.access_ssh
```

Woah!  That's a lot...you should be fine if you choose `staff` or `everyone` for this exercise.  For example, since my username on mac is `sven`, then I executed

```
>>> sudo chown -R sven:everyone demo/
>>> ls -lR demo/
total 0
drwxr-xr-x  3 sven  everyone  102 Feb  4 13:45 lemmings

demo//lemmings:
total 8
-r--r--r--  1 sven  everyone  15 Feb  4 13:45 are_watching_you.txt
>>> mv demo/lemmings/are_watching_you.txt demo/
>>> ls -lR demo/
total 8
-r--r--r--  1 sven  everyone  15 Feb  4 13:45 are_watching_you.txt
drwxr-xr-x  2 sven  everyone  68 Feb  4 14:20 lemmings

demo//lemmings:
```

I hope you had fun with this exercise, as well as got a better understanding for how permissions work as well as how different Unix systems can be!
