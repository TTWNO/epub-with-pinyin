#!/bin/bash

fullfilename="$1"
extension="${fullfilename##*.}"
filename="${fullfilename%.*}"

mkdir -p "$filename"
cd "$filename"
unzip -q "../$fullfilename"
cd ..

mkdir -p "$filename-with-pinyin"
cp -r "$filename" "$filename-with-pinyin"
mkdir -p "$filename-with-pinyin/$filename/OEBPS/js" || mkdir -p "$filename-with-pinyin/$filename/OPS/js" && echo "Alternate path found"
cp "js/functions.js" "$filename-with-pinyin/$filename/OEBPS/js/" || cp "js/functions.js" "$filename-with-pinyin/$filename/OPS/js/" && echo "Alternate path found"

echo "Starting the Python program:"
if command -v uv &> /dev/null; then
    uv run main.py "$fullfilename"
else
    python3 main.py "$fullfilename"
fi

echo "Creating new epub file"
cd "$filename-with-pinyin"
cd "$filename"

zip -r -q "../../$filename-with-pinyin.epub" *
cd ../..
echo "Done...Cleanup now."

rm -r "$filename-with-pinyin" "$filename"
echo "Done cleaning."
echo "Done."
