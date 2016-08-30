### easy_depencencies_linux.py ###

git clone https://github.com/TTWNO/dragonmapper
cd dragonmapper
python3 setup.py install
cd ..
rm -rf dragonmapper

pip3 install jieba
pip3 install beautifulsoup4
pip3 install ebooklib

wget https://raw.githubusercontent.com/fxsjy/jieba/master/extra_dict/dict.txt.big
