> # Counting and Sorting, Committing to your Changes
>
> You now have the file `frankenstein.txt` in this directory.  Fill in each `p*.sh` with a *minimal* script (most can be one line).  When you are done, make each `p*.sh` executable, commit, and push your changes to your forked repository.
>
> ## p1.sh
>
> Calculate the minimum used word in `frankenstein.txt`.

First, we need to make sure we do not count capitalizations as separate words.  That is, `This` is the same as `this` is the same as `tHiS`.  We can do this use the `tr` tool to tralsnate all uppercase letters to lower case letters:

```bash
cat frankenstein.txt | tr "[:upper:]" "[:lower:]"
```

From here, we want to count the number of occurrences of each word. This is  slightly more involved, but we can start by making a list of all words in the file -- including duplicates.

```bash
cat frankenstein.txt | tr "[:upper:]" "[:lower:]" | tr -c "[:alnum:]" "\n" | grep -v "^$"
```

We use `tr` to translate all non-alphanumeric characters (using the `-c` flag) to newlines, and then use `grep` to strip off any resulting blank lines.

Now, we want to sort the list  we've created and count adjacent occurrences to find the least used word. The `uniq -c` command will let us do that, but we need to `sort` the list first, giving us the final command:

```bash
cat frankenstein.txt | tr "[:upper:]" "[:lower:]" | tr -c "[:alnum:]" '\n' | grep -v "^$" | sort | uniq -c | sort -n
```

Lastly, we can just take the first element of this list using `head -n 1`, and the final script contents would just be:

---
**p1.sh**
```bash
#!/bin/bash

cat frankenstein.txt | tr '[[:upper:]]' '[[:lower:]]' | tr -c '[[:alnum:]]' '\n' | grep -v "^$" | sort | uniq -c | sort -n | head -n 1
```

---

However, if you look at `head -n 4`, you will see that all them were counted equally -- any one of the ones in this list would technically be a valid answer.  As it turns out, this will give us the first word that was found twice:

```bash
tr "[:upper:]" "[:lower:]" < frankenstein.txt | tr -c "[:alnum:]" '\n' | grep -v "^$" | sort | uniq -c | sort -n | head -n 3113
```

Palindrome by chance? I think not.  I threw in the `tr "[:upper:]" "[:lower:]" < frankenstein.txt` at the beginning instead of using `cat` just to give an example of how you can use the `<` for file input, even if you are piping things.

> ## p2.sh
>
> Calculate the maximum used character in `frankenstein.txt`.

This exercise is similar to the previous, the only difference is the setup.  We now want to have each character on its own line, rather than each line.  There are many ways to do this, but the to simplest would be

1. `grep -o "." frankenstein.txt`

    The `-o` option says "only match", but we combine this with the wildcard for regular expressions `.` to say match anything.  Recall that in your shell the `*` is the wildcard, but for `grep` it is `.`, and when using the `*` that is what is called a glob.  The `*` glob says **0** or more instances.

2. `fold -w 1 frankenstein.txt` (read the man page for `fold`).

---

**p2.sh**
```bash
#!/bin/bash

grep -o "." frankenstein.txt | sort | uniq -c | sort -n
```

---

Giving us that the most frequently used character is the space character, followed by the `e` character.

> ## p3.sh
>
> Calculate the number of times the word `monster` appears in `frankenstein.txt`.

Using `grep` we can count the number of times `monster` appears directly using the `-c` flag.  Since we want to just find the word without any partial matches, we can include the `-o` flag again.

---

**p3.sh**
```bash
#!/bin/bash

grep -co "monster" frankenstein.txt 
```

---

Revealing that the word `monster` appears **33** times in the text.

> ## p4.sh
>
> Extract the 10 most used words in Letter 3 of `frankenstein.txt`.  Words should contain no punctuation marks and the different forms of words with capital and lower case letters should be considered the same word, e.g., "The" and "the" are the same words, and "tree!" and "man," are not words, but the trimmed version "tree" and "man" are.
>
> Hint: Letter 3 is between lines 255 and 298 of the file frankenstein.txt.

Combining all of our tricks so far, the only thing we need to note here is that we first need to seek to the appropriate location in the file before we can begin any processing.  The first two commands simply grab all of the first 298 lines, and then trim off the last 43.  Lastly, the `head` command defaults to 10, so we do not necessarily need to specify the `-n` flag here.

---
**p4.sh**
```bash
#!/bin/bash

head -n 298 frankenstein.txt | tail -n 43 | tr "[:upper:]" "[:lower:]" | tr -c "[:alnum:]" "\n" | grep -v "^$" | sort | uniq -c | sort -nr | head
```

---
