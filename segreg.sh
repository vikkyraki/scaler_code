#!/bin/bash

cd segregate_photos

files=$(ls)
cd "../photos"


for file in $files;
do
		if [ "$file" == "README.md" ]
		then
			continue
		fi
        year=${file:0:4}
        month=${file:5:1}

        mkdir "$year"
        cd "$year"

        mkdir "$month"
        cd "$month"

        count=$(ls -lr | wc -l)
       	file_name="photo$count.jpeg"

        cp "/home/kota/Documents/scaler_code/segregate_photos/$file" "$file_name"
        cd ../..

done     