#!/bin/bash

fullfilename="$1"
extension="${fullfilename##*.}"
filename="${fullfilename%.*}"

mkdir "$filename"
cd "$filename"
unzip -q "../$fullfilename"
cd ..

mkdir "$filename-with-pinyin"
cp -r "$filename" "$filename-with-pinyin"
mkdir "$filename-with-pinyin/$filename/OEBPS/js"
cp "js/functions.js" "$filename-with-pinyin/$filename/OEBPS/js/"

echo "Starting the python3 program:"
python3 main.py "$fullfilename"

echo "Creating new epub file"
cd "$filename-with-pinyin"
cd "$filename"

zip -r -q "../../$filename-with-pinyin.epub" *
cd ../..
echo "Done...Cleanup now."

rm -r "$filename-with-pinyin" "$filename"
echo "Done cleaning."
echo "Done."
