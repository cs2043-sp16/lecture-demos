# lecture-demos

Lecture demos for [CS 2043][cs2043].

You are in no way expected to complete all of these exercises, they are here for you to experiment if you want
to.  We will begin the exercise at the end of class, and I will release *a* solution (not *the only* solution)
at some point soon after the demo is presented during class.

If you are uninterested, have something else you need to do, finish early, etc, you do not have to stay until
class is done.  Use these demos as a resource.

Contributions are welcome in the form of Pull Requests.

[cs2043]: http://cs2043-sp16.github.io/

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

## How do I get this on my computer?!

Initially, you will have to `clone` this repository.  The following example shows you how to put it on your
Desktop, but you can have it anywhere you want.

```
>>> cd ~/Desktop/
>>> git clone https://github.com/cs2043-sp16/lecture-demos.git
```

You now have the folder `~/Desktop/lecture-demos/`.  To work on a specific exercise, simply `cd` into the
directory.  For example, if you want to work on the exercise for lecture 3, you will find it at

```
>>> cd ~/Desktop/lecture-demos/lec03/
```

Since you were already at `~/Desktop/`, though, you could also just `cd lecture-demos/lec03` to work on that
specific exercise.

## When the next lecture's demo is added, how do I get it?

You now have a *local* copy of the demo repository on your computer.  Unlike Dropbox, `git` does not automatically
download things for you.  Remember that `.git/` folder?  That is where the magic happens.  Do not **ever** change,
delete, or add anything in this folder.  When you do

```
>>> cd ~/Desktop/lecture-demos/
>>> ls -al
```

you will see the `.git` folder.  This means that you are at the *top-level* directory of a `git` repository.  Now
you can issue the

```
>>> git pull
```

command, and if the remote server has any updates on it you will be able to download them locally.  As long as
you are in the `lecture-demos` or any of its subdirectories, you can execute the above command to get new files!

## Great, but how do I keep track of my own changes?

You are welcome to work locally, you can `git commit` your changes and they will be saved.

Go to [lecture 4's demo](lec04/) to see how to setup the a fork so you can get practice making commits and pushing to a repository.

I will (hopefully) not ever need to make any changes directly to the original files I push for each lecture demo,
and will instead be creating `SOLUTION` files / folders where applicable.  As long as you do not ever make a file
or folder named `SOLUTION` (e.g. `SOLUTION.md`, `SOLUTION.sh`, `SOLUTION/`, etc), you should not have any merge conflicts
when you do `git pull`.
