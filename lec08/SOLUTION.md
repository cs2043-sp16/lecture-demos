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