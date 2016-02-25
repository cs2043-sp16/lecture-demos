#!/bin/bash

IFS=''

while read line; do
    echo "Len [${#line}]: $line"
done < "$1"
