# Scripting with Sed

In this exercise you will create a simple script `nav.sh` that will convert `base.html` into four separate files: `home.html`, `about.html`, `work.html`, and `play.html`.

## Contents of Base

The contents of `base.html` have two formats that need to be changed.

### Navbar

The first item of concern is the "navbar".  You don't need to know anything about html to complete this exercise.  The navbar in `base.html` looks like this:

```html
<div id="header">
    <nav id="nav">
        <ul>
            <li><a href="home.html">Home</a></li>
            <li><a href="about.html">About</a></li>
            <li><a href="work.html">Work</a></li>
            <li><a href="play.html">Play</a></li>
        </ul>
    </nav>
</div>
```

For each element in `{home,about,work,play}` you need to change the `<li>` element to become `<li class="current">`.  For example, the `home.html` would be

```html
<div id="header">
    <nav id="nav">
        <ul>
            <li class="current"><a href="home.html">Home</a></li>
            <li><a href="about.html">About</a></li>
            <li><a href="work.html">Work</a></li>
            <li><a href="play.html">Play</a></li>
        </ul>
    </nav>
</div>
```

and the `about.html` page should be

```html
<div id="header">
    <nav id="nav">
        <ul>
            <li><a href="home.html">Home</a></li>
            <li class="current"><a href="about.html">About</a></li>
            <li><a href="work.html">Work</a></li>
            <li><a href="play.html">Play</a></li>
        </ul>
    </nav>
</div>
```

### Text replacement

The `base.html` also has a large number of `[[[###]]]` pasted throughout.  You are to replace each one of these with one of `{home,about,work,play}`, depending on which one you are working on.

## Creating the new Pages

You should write a shell script `nav.sh` that assumes `base.html` is in the same directory.  This script is to loop over `{home,about,work,play}` and make the desired replacements, saving those replacements into `home.html`, `about.html`, `work.html`, and `play.html` respectively.

The solution is being released with the demo, but do try and write it on your own though!

### Tips on Approaching this Problem

1. Start by working with just one of them.  For example, only focus on creating `home.html`.
2. Figure out how to change the `navbar` described above, just having it print to the console.
3. When you think you have it, redirect that to `home.html` and open it in your browser.  If `Home` at the top is highlighted in red, then you did this correctly!
4. Figure out how to replace the `[[[###]]]` with `home`.
5. Figure out how to execute two replacements with `sed`.
   - You can use the `-e` flag to signal a script.
   - You do not have to actually write a separate file; the script can be inline.
   - Separate replacements with a `;`
6. Put it all in a loop!
   - Maybe try writing a loop to `echo` out `{home,about,work,play}` first.
7. Be very careful with single vs double quotes.  I heavily emphasized in lecture that you should try and always use single quotes.  Which is true.  But you should not complete this exercise using just single quotes.
   - If you have a variable `FOO` and try and create a string using `'Hi $FOO, how are you?'`, it will not work.  You will get `$FOO`, not the value in `FOO`.
   - One solution is to write `'Hi '"$FOO"', how are you?'`
   - I told you, `bash` is rarely pretty.
   - <a href="http://stackoverflow.com/a/13802438/3814202" target="_blank">This SO answer</a> gives a good explanation of why.  Single quotes preserve everything!

### When you are Finished

Go ahead and `git add` your `nav.sh` script, as well as the beautiful new html files you have generated automatically!

Follow it all up with a `git commit` and `git push` to store your work online!
