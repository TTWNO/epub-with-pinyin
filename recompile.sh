rm -r out.epub
./add-pinyin.sh $1
mkdir out.epub
cd out.epub
unzip "../${1%.*}-with-pinyin.epub"
