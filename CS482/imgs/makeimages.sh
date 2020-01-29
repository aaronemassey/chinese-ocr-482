#!/bin/bash
LANG=en_US.UTF-8;
for file in ./../text/*.txt; do 
	for char in $(cat $file | sed -e 's/\(.\)/\1\n/g');
	do convert -size 80x80 -depth 8 pattern:GRAY100 -gravity center -font WenQuanYi-Micro-Hei -pointsize 64 -encoding Unicode -draw "text 0,0 '$char'" $char.jpg;
	done 
done

