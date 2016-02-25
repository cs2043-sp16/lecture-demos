# Scripting with Sed

The solution script is as follows:

```bash
#!/bin/bash

for page in {home,about,work,play}; do
    # identify the pattern we are searching for with the navbar
    NAV_PATTERN="<li><a href=\"$page.html\""
    NAV_REPLACE="<li class=\"current\"><a href=\"$page.html\""

    # write out the replacements
    TAG="\[\[\[###\]\]\]"
    REP="$page"
    sed -e 's/'"$NAV_PATTERN"'/'"$NAV_REPLACE"'/g; s/'"$TAG"'/'"$REP"'/g' < base.html > "$page".html
done
```

Basically, we have to search for the common items in both and replace them.  Four new html files will be generated, and you can open one of `home.html`, `about.html`, `work.html`, or `play.html` in your browser and navigate between them :)


## Notes

The solution above uses the `-e` (lower case) flag.  The `-e` flag indicates a "script" is going to be provided to `sed`.  I wrote a script "in-line", aka it was not in a separate file, but this flag could also be used followed by a filename (that contains the script).  Where assignment 2 is concerned, you are allowed to write an in-line script if you so choose, but all of your code must remain in one file.

### What makes it an in-line script?

---------------------------------------------------------------------------------------------------------------------------------------------

To be explicit, the "in-line" script is really just the fact that I provided two substitutions separated by a `;`

```bash
#                                           vvv
sed -e 's/'"$NAV_PATTERN"'/'"$NAV_REPLACE"'/g; s/'"$TAG"'/'"$REP"'/g' < base.html > "$page".html
#                                           ^^^
```

I could have just as easily piped my first replacement to my second replacement to get the same result:

```bash
sed 's/'"$NAV_PATTERN"'/'"$NAV_REPLACE"'/g' < base.html | sed 's/'"$TAG"'/'"$REP"'/g' > "$page".html
```

Notice, though, that this is no longer a script and therefore I have removed the `-e` flag.

### Alternations

---------------------------------------------------------------------------------------------------------------------------------------------

You may find that you have many `sed` commands to execute, and your lines are getting very long and annoying because you have to scroll horizontally.  Remember that you can use the continuation character `\` to continue writing on the next line.  I suggest only using this character after a pipe character to maintain code clarity.  Many encourage no more than `80` characters per line, but I often find that unreasonable (especially if I am doing `namespace::someMethod()` all over the place in `C++` or something).  I tend to try and have no more than `111` characters on a line.  Example continuation of the above:

```bash
sed 's/'"$NAV_PATTERN"'/'"$NAV_REPLACE"'/g' < base.html | \
    sed 's/'"$TAG"'/'"$REP"'/g' > "$page".html
```

Note that I indented the continued line further than the original.  This is not necessary, but helps *you* keep track of what is where.  Additionally, you can do this as many times as you want, and can even line up all of your pipes and continuations to make it even more beautiful:

```bash
# Lets go ahead and quadruple this all...notice that I used
# the -E on the last sed because MORE is an extended regex.
# Recall that though not officially in the man page, -E is
# equivalent to -r on GNU sed, but BSD/OSX sed does not have
# -r so we elect to use -E for portability.
MORE="<li>($page+.*)<\/li>"
sed 's/'"$NAV_PATTERN"'/'"$NAV_REPLACE"'/g' < base.html | \
    sed 's/'"$TAG"'/'"$REP"'/g'                         | \
    sed -E 's/'"$MORE"'/<li>\1 \1 \1 \1<\/li>/g'        > "$page".html
```

This saved everything in the parentheses as `\1` (since I only had one group of parentheses), and I can use it as many times as I want.

### Use Caution Mixing Single and Double Quotes!

---------------------------------------------------------------------------------------------------------------------------------------------

Be on the lookout:

1. Use caution: note that the regex is defined in *double quotes*.
2. Likewise, the *single quote* should be used with the string to `sed`, but in order to dereference the value of say `NAV_PATTERN`, you have to end the single quote string and get the value with `"$NAV_PATTERN"` in double quotes.  Then begin the *single quote* string again.
3. Though this is a bit verbose, and not the only way, it gives you a higher probability of success.
4. Refer to the preamble for how to debug your scripts using the `set` command.

### Making `sed` More Convenient

---------------------------------------------------------------------------------------------------------------------------------------------

Last but certainly not least, notice that I had to escape the ending html tag `<\/li>` because with `sed` we are delineating our replacement strings with the `/` character.  You actually do **not** have to use a `/`, and in the case of modifying html code the `/` character can be rather inconvenient.  As far as how we are using `sed` in this class, you basically just specify what your separator is after the `s`.  Working with the last example, we can now do

```bash
MORE="<li>($page+.*)</li>"
    sed 's@'"$NAV_PATTERN"'@'"$NAV_REPLACE"'@g' < base.html | \
        sed 's@'"$TAG"'@'"$REP"'@g'                         | \
        sed -E 's@'"$MORE"'@<li>\1 \1 \1 \1</li>@g'         > "$page".html
```

and I can get away with typing `</li>` without escaping it because our separator is now `@` instead of `/`, and `sed` won't get confused!  Note that you don't have to use the same separator for every call to `sed`, it will just look at the character after the `s` at the beginning and say "Ok this is my separator."

Though there are extra rules associated with this, you can indeed use a different delimiter!  Read <a href="http://backreference.org/2010/02/20/using-different-delimiters-in-sed/" target="_blank">this article</a> to see your options.  **Note:** I *strongly* discourage using a space character, that will almost certainly cause you grief.
