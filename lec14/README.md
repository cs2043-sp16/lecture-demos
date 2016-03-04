# Debugging Python3

Now that you have followed your system-specific `python3` installation instructions, and installed `ipdb` using `pip3`, you should be able to just execute this script with

```bash
>>> ./debug.py
```

Note that if you are unable to run it, this is because `python3` is not showing up in your `$PATH` correctly for some reason.  If you are confident that you have it installed, just do

```bash
>>> python3 debug.py
```

If you decided not to install `python3`, then you should be able to execute the `pip` installation (not `pip3`) at the end of lecture 14 in order to get `ipdb`.  You will just need to change the shebang at the top of the file, or run `python debug.py`.

## What is a Debugger?

The short version is that a debugger lets you step through your code line by line, or function call by function call, or by setting breakpoints, and many many other useful features.  While I won't cover debuggers any more in this class, you should familiarize yourself with how to properly debug your code.

Yes, many times you can get away with print statements and carry on.  We all do it.  But there will be times that you just can't find the bug this way.  Debuggers allow you to step through the code as it executes, and is an essential tool for any developer.  `ipdb` is an interactive Python debugger, very similar in nature to `gdb` for C/C++ in terms of the commands you type.  `ipdb` is superior to `pdb` only in that the output is colorized, and a lot easier to follow!

## First Run

Lets run the script without debugging, just to see what happens.  It is supposed to just transpose a simple matrix:

```bash
>>> ./debug.py
Before transpose:
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
------------------
After transpose:
[0, 0, 0, 0, 0]
[0, 1, 1, 1, 1]
[0, 1, 2, 2, 2]
[0, 1, 2, 3, 3]
[0, 1, 2, 3, 4]
```

Clearly that wasn't a transpose!  The code is simple enough that you can probably see the error by inspection (especially if you have written a `swap` function before).  We forgot to store the value in a temporary value, and it got overwritten x0.  But lets debug it using `ipdb` following the directions at the top of the file to get some experience with a relatively straight-forward example to kickstart our debugging career.

## Debug Run

I am just going to paste the output of what my debugger is showing me now, but you should follow the instructions at the top of `debug.py` yourself to get the full experience (including the coloring, which GitHub Markdown is not going to show in the same way).

I un-comment line 25 `ipdb.set_trace()` in order tell `ipdb` that we want to start debugging there.  You can move that call anywhere you want, as well as do a whole lot more with `ipdb`.  Technically this is the `IPython` debugger, but it functions just the same as `pdb` and is a little easier to follow in my opinion ;)

```bash
lecture-demos/lec14> ./debug.py
Before transpose:
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
> lecture-demos/lec14/debug.py(65)<module>()
     64 #
---> 65 for x in range(N):
     66     for y in range(N):

ipdb> s
> lecture-demos/lec14/debug.py(66)<module>()
     65 for x in range(N):
---> 66     for y in range(N):
     67         mat[x][y] = mat[y][x]

ipdb> p x
0
ipdb> s
> lecture-demos/lec14/debug.py(67)<module>()
     66     for y in range(N):
---> 67         mat[x][y] = mat[y][x]
     68         mat[y][x] = mat[x][y]

ipdb> p y
0
ipdb> s
> lecture-demos/lec14/debug.py(68)<module>()
     67         mat[x][y] = mat[y][x]
---> 68         mat[y][x] = mat[x][y]
     69

ipdb> s
> lecture-demos/lec14/debug.py(66)<module>()
     65 for x in range(N):
---> 66     for y in range(N):
     67         mat[x][y] = mat[y][x]

ipdb> s
> lecture-demos/lec14/debug.py(67)<module>()
     66     for y in range(N):
---> 67         mat[x][y] = mat[y][x]
     68         mat[y][x] = mat[x][y]

ipdb> p x
0
ipdb> p y
1
ipdb> p mat[x][y]
1
ipdb> p mat[y][x]
0
ipdb> s
> lecture-demos/lec14/debug.py(68)<module>()
     67         mat[x][y] = mat[y][x]
---> 68         mat[y][x] = mat[x][y]
     69

ipdb> s
> lecture-demos/lec14/debug.py(66)<module>()
     65 for x in range(N):
---> 66     for y in range(N):
     67         mat[x][y] = mat[y][x]

ipdb> p x
0
ipdb> p y
1
ipdb> p mat[x][y]
0
ipdb> p mat[y][x]
0
ipdb> exit()
Exiting Debugger.
```

## Found the bug!

Sweet, we found the bug.  Fix the swapping in the loop to use a temporary variable, then commit and push your changes online!
