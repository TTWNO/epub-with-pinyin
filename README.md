# epub-pinyin
Adds Pinyin to .epub files

# Requirements
* https://github.com/TTWNO/dragonmapper develop branch>
* BeautifulSoup4
* https://github.com/tsroten/pynlpir
* python(3) ebooklib

# Usage:

./add_pinyin.sh test.epub

New file will be saved as test-with-pinyin.epub
Report errors to: taitskywalker@gmail.com

# TIP:
* run update_dict.py ONCE with admin privilages to add words from CEDICT-ts.u8
* do so again to update with new words from the file.
