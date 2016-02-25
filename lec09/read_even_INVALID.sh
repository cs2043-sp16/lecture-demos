#!/bin/bash

IFS=''

while read line || [[ -n "$line" ]]; do
    echo "Len [${#line}]: $line"
done < "$1"
