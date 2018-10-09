#!/bin/bash

command <<HERE
for f in *; do
	echo "$f"
	extension="${f##*.}"
	filename="${f%.*}"
	echo "$extension"
	echo "$filename"
	echo
done
HERE

for f in *.epw; do
	filename="${f%.*}"
	mkdir temp
	cd temp
	energyplus -w "../$f" -p $filename -s C -x -m -r ../Model7.idf
	#echo "$filename.htm"
	cp ""$filename"Table.htm" ~/all_html/
	cd ..
	rm -rf temp
done
