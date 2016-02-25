#!/bin/bash

while read line; do
    echo "Len [${#line}]: $line"
done < "$1"
