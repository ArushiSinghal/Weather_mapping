#!/bin/sh

for d in ./tempDir/*/ ; do
    #echo "Number of files in $d is $(find "$d" -type f | wc -l)"
    a=$(find "$d" -type f | wc -l)
    #echo "$a"
    if [ $a -eq 0 ]
    then
        echo "Number of files in $d is $a"
    fi
    if [ $a -gt 1 ]
    then
        echo "Number of files in $d is $a"
    fi
done
