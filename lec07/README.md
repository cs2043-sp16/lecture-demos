# Job Control

In this exercise you will not need to change / add anything to your repository, just be ready to play with your terminal.  We will be working with `vlc` because I think it is a really good way to undertand when jobs are running / paused (since you can hear the music stop).  This is basically just a transcript of what I showed you in class.

## Install VLC if you Haven't Already

The `vlc` media player is rather powerful, and can understand a wide-range of different filetypes.  It really is a wonderful little tool.

### Mac OSX

We have not covered package managers yet, but `vlc` is available through `homebrew`.  Alternatively, you can just go to the official download page [here](http://www.videolan.org/vlc/download-macosx.html).

### Fedora

You should be able to execute

```bash
>>> sudo dnf install vlc
```

### Ubuntu

You should be able to execute

```bash
>>> sudo apt-get install vlc
```
 but I believe Ubuntu ships with `vlc` these days.

 ### Linux note:

 By default the linux kernel does not ship with support for various types such as `mp3`, for legal reasons.  I have already setup both of the virtual machines to have support for the common codecs.  It's easy these days:

   - Fedora: I used `Fedy` to do the work.
   - Ubuntu: When you install it prompts you if you would like them to download these for you while it is getting setup.

## Using VLC From the Command Line

### Navigate to a Directory with Some Music

If you really can't decide what to listen to, maybe *Menik* has the solution for you.  Go ahead and grab it from <a href="https://soundcloud.com/bigupmagazine/big-up-mix-94-menik" target="_blank">Soundcloud</a>.  May not be your cup of tea though...

The download button on that page will give you a file named *Big Up Mix 94 - Menik.mp3*.  I will continue with that as the example file, but if you are in a directory with multiple mp3 files you can easily just do `*.mp3`.  The song title I have chosen has the added benefit that you will greatly appreciate your `TAB` key now...because the spaces require that you actually type `Big\ Up\ Mix\ 94\ -\ Menik.mp3`........so use that `TAB` key!

### The Executable

- On almost every Linux OS, you can simply type `vlc`.  You can execute `which vlc` to see where it actually is, but just `vlc` by itself should be good enough.

- On OSX, however, things are a little different.  If you installed it in the standard `Applications` folder, then the path to your binary executable should be `/Applications/VLC.app/Contents/MacOS/VLC`

I will only be including the Linux version, but just remember that you need to type that whole thing as `vlc` will not be a command for you.  Though you could also very easily make an `alias` (see Lecture 06 demo) to make your life better.

### Play a File with VLC

As easy as:

```bash
>>> vlc Big\ Up\ Mix\ 94\ -\ Menik.mp3
```

You should now be hearing something coming through your speakers / headphones.

**Caution**: `vlc` has some serious problems if you give invalid filenames.

1. Use the `TAB` key to guarantee that is correct.
2. `ctrl+c` may work for you, try that first.
3. You very well may need to `kill` it, and it almost certainly will not go quietly.  Another reason I chose this.

    ```bash
    # Get the PID, copy paste that (it should be the first number, mine was 8295 but yours will be different).
    >>> ps -e | grep -i vlc
    # Really really kill it dead.  Make sure you use the right PID...
    >>> sudo kill -9 8295
    ```

### Pausing a Running Process

Because we did not launch our process with an `&` after it, it is in the foreground.  `vlc` likely spat out some colorful output.  To pause the process, we use `ctrl+z` (that is control on Linux *and* OSX).  My output looked like this

```bash
>>> vlc Big\ Up\ Mix\ 94\ -\ Menik.mp3
VLC media player 2.2.2 Weatherwax (revision 2.2.1-161-g360f42e)
[00000000006ea118] core libvlc: Running vlc with the default interface. Use 'cvlc' to use vlc without interface.
TagLib: ID3v2.4 no longer supports the frame type TDA.  It will be discarded from the tag.
TagLib: ID3v2.4 no longer supports the frame type TIM.  It will be discarded from the tag.
TagLib: ID3v2.4 no longer supports the frame type TDA.  It will be discarded from the tag.
TagLib: ID3v2.4 no longer supports the frame type TIM.  It will be discarded from the tag.
#
# adding space for emphasis, just type ctrl+z
#
^Z
[1]+  Stopped                 vlc Big\ Up\ Mix\ 94\ -\ Menik.mp3
```

### Resuming a Process

We now have a process paused, and want to know more about it.

```bash
>>> jobs
[1]+  Stopped                 vlc Big\ Up\ Mix\ 94\ -\ Menik.mp3
```

The `jobs` command reveals that it is still there, but is not currently running.  To resume it, we can either put it in the foreground or the background.  Lets do the foreground first.

```bash
>>> fg %1
vlc Big\ Up\ Mix\ 94\ -\ Menik.mp3
[00007f92a40009b8] core input error: ES_OUT_SET_(GROUP_)PCR  is called too late (pts_delay increased to 300 ms)
[00007f92a40009b8] core input error: ES_OUT_RESET_PCR called
```

And it starts playing again.  The `%1` specifically refers to job `1`, if we were trying to do something with job `4` then you would use `%4`.  If you do not specify a number, `%%` is assumed, which means `use the last one`.

Now lets go ahead and put it in the background.

```bash
# previous output from fg duplicated
vlc Big\ Up\ Mix\ 94\ -\ Menik.mp3
[00007f92a40009b8] core input error: ES_OUT_SET_(GROUP_)PCR  is called too late (pts_delay increased to 300 ms)
[00007f92a40009b8] core input error: ES_OUT_RESET_PCR called
#
# adding space for emphasis again
#
^Z
[1]+  Stopped                 vlc Big\ Up\ Mix\ 94\ -\ Menik.mp3
# confirm
>>> jobs
[1]+  Stopped                 vlc Big\ Up\ Mix\ 94\ -\ Menik.mp3
>>> bg %1
[1]+ vlc Big\ Up\ Mix\ 94\ -\ Menik.mp3 &
[00007f92a40009b8] core input error: ES_OUT_SET_(GROUP_)PCR  is called too late (jitter of 104523 ms ignored)
```

Notice this time a little `&` got put in at the end.

### Problems

If you were to close your terminal right now (on Linux, OSX this is not the case for more complicated reasons than I care to explain) then `vlc` would close and you would never find out exactly where you stopped watching your Lord of the Rings marathon.  Not cool.  Since our job is already running, we are going to `disown` it so that when we close our terminal `vlc` stays alive.

```bash
>>> jobs
[1]+  Running                 vlc Big\ Up\ Mix\ 94\ -\ Menik.mp3 &
>>> disown -h %1
```

Now if you close your terminal, `vlc` should stay alive.  Go ahead and launch vlc from your terminal without `disown`ing it to observe what happens if you do not.

Note that you can launch commands to behave this way by default using `nohup`, e.g. if I do

```bash
>>> nohup vlc Big\ Up\ Mix\ 94\ -\ Menik.mp3 &
[1] 18497
nohup: ignoring input and appending output to ‘nohup.out’
#
# hit the skip forward track button a bunch of times
#
>>> cat nohup.out
TagLib: ID3v2.4 no longer supports the frame type TDA.  It will be discarded from the tag.
TagLib: ID3v2.4 no longer supports the frame type TIM.  It will be discarded from the tag.
TagLib: ID3v2.4 no longer supports the frame type TDA.  It will be discarded from the tag.
TagLib: ID3v2.4 no longer supports the frame type TIM.  It will be discarded from the tag.
TagLib: ID3v2.4 no longer supports the frame type TDA.  It will be discarded from the tag.
TagLib: ID3v2.4 no longer supports the frame type TIM.  It will be discarded from the tag.
TagLib: ID3v2.4 no longer supports the frame type TDA.  It will be discarded from the tag.
TagLib: ID3v2.4 no longer supports the frame type TIM.  It will be discarded from the tag.
TagLib: ID3v2.4 no longer supports the frame type TDA.  It will be discarded from the tag.
TagLib: ID3v2.4 no longer supports the frame type TIM.  It will be discarded from the tag.
TagLib: ID3v2.4 no longer supports the frame type TDA.  It will be discarded from the tag.
TagLib: ID3v2.4 no longer supports the frame type TIM.  It will be discarded from the tag.
.
.
.
```

So great, I can make it so that I can close my terminal and keep `vlc` running, but now this `nohup.out` file is being generated.  The `vlc` executable is quite verbose, the last thing you want is a bunch of random `nohup.out` files lying around.  While that may be less annoying than having that output to the terminal, we can do better.

### Solutions

The last thing we need here is to just redirect things!

#### Linux (needs bash 4.0+)

If you run `bash --version` and get a number greater than or equal to `4.0`, then you can use the non-POSIX compliant but much easier to remember syntax:

```bash
>>> nohup vlc Big\ Up\ Mix\ 94\ -\ Menik.mp3 &> /dev/null &
[1] 18885
>>> jobs
[1]+  Running                 nohup vlc Big\ Up\ Mix\ 94\ -\ Menik.mp3 &> /dev/null &

```

Note that if you close the terminal, though, you will still be listening to your awesome music.  Furthermore, when you open a new terminal and execute `jobs` it will not be there.  Be aware that backgrounding jobs and forgetting about them can be cumbersome to resolve.



#### OSX

Unless you have gone through and installed a new version of bash, you likely do not have higher than 4.0.  So you would execute something like

```bash
nohup /Applications/VLC.app/Contents/MacOS/VLC  Big\ Up\ Mix\ 94\ -\ Menik.mp3 > /dev/null 2>&1 &
```

First you need to redirect standard output to `/dev/null`, and then say "send error where out is going" with `2>&1`.  Last but not least, putting it in the background with an `&`.

Technically you do not need to have the `nohup`.  If you did not use it, when you quit your terminal it will say "Hey you're still running vlc", but if you close anyway then VLC will keep running.  Mac does some fancy stuff.  But if you include the `nohup` then it will not give you that warning.

### Making Life Easier

I have added a new component to my `~/.bashrc` that is like an alias, only it can take arguments (a function).

#### Linux

```bash
vlc () {
    nohup $(which vlc) "$@" &>/dev/null &
}
```

#### OSX

```bash
vlc () {
    nohup /Applications/VLC.app/Contents/MacOS/VLC "$@" > /dev/null 2>&1 &
}
```

#### Explanation

Functions can take in arguments.  You would access the first one with `$1`, the second with `$2`, etc.  The `$@` says "expand all arguments", which is needed if you want to do `vlc *.mp3`.  Don't forget you need to `source ~/.bashrc` to use it immediately.
