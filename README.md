# epub-pinyin
Adds Chinese phonetic scripts to .epub files

* Pinyin
* Jyutping (comming soon)

# Requirements
* [uv](https://docs.astral.sh/uv/)

or

* https://github.com/TTWNO/dragonmapper <develop branch>
* python(3) beautifulsoup4
* python(3) jieba
* python(3) ebooklib
* python(3) lxml

# Installation

* If you are using [`uv`](https://docs.astral.sh/uv/), just make sure `uv` is installed and there is nothing else to do.

* If you are on Linux, and are using python3

```bash
sudo easy_dependencies_linux_python3.sh
```

* For everyone else, or to do it manually

```bash
git clone https://github.com/TTWNO/dragonmapper.git
cd dragonmapper
git checkout develop
setup.py install
rm -rf dragonmapper

pip install -r requirements.txt
```

# Usage:

./add_pinyin.sh foobar.epub

New file will be saved as foobar-with-pinyin.epub
Report errors to: taitskywalker@gmail.com || use issues tab.
