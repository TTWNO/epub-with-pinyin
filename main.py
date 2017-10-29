#!/bin/python3.4
# -*- coding: utf-8 -*-
"""A Python app that makes epub files with pinyin in them."""

import sys
import html as htmlLib
import os

from dragonmapper import transcriptions as trans
from dragonmapper import hanzi
from dragonmapper import html
import hanzidentifier as ziid
from ebooklib import epub
import jieba

from bs4 import BeautifulSoup
import bs4

# Change These #
debug_is_on = False
numbered_pinyin = False

dict_file = './dict.txt.big'

# \Change These #

FULL_FILE_NAME = sys.argv[1]
FILE_NAME, FILE_EXT = FULL_FILE_NAME.split('.')
NEW_DIR = FILE_NAME + '-with-pinyin'

EPUB_BLACKLIST_KEYWORDS = ['pagenav']

GET_TAG_NAMES = ['p', 'strong', 'h1',
                 'h2', 'h3', 'h4',
                 'h5', 'h6', 'i',
                 'b', 'u', 'a', 'em']


def is_entirely_chinese(s):
    """
    Check if every character in the string is Chinese.

    *s* string to search in
    """
    debug('TEST(IEC): '+str(s))
    for c in s:
        if not ziid.has_chinese(c):
            debug('TEST(IEC): '+c+' is not chinese.')
            return False
    return True


def debug(s):
    """
    Print info to screen, but only when debugging is enabled.

    *s* object to print
    """
    if debug_is_on:
        print(s)


def find(name, path):
    """
    Look for, and return (if found) the path of a file.

    *name* name of the file
    *path* directory to look in
    """
    for root, drs, fls in os.walk(path):
        debug('ROOT: {0}\nDIRS: {1}\nFILES: {2}'.format(root, drs, fls))
        if name in fls:
            return os.path.join(root, name)


def find_epub_files(f):
    """
    Get list of files needed to be converted.

    *f* epub file no extention
    """
    all_star_html = []
    book = epub.read_epub(f + '.epub')
    for t in book.toc:
        debug(t.href)
        debug(f)
        t_href = t.href
        file_dot_index = t_href.rfind('.')
        t_name = t_href[:file_dot_index]
        t_ext = t_href[file_dot_index:]

        stn_file = t_name + t_ext
        extr_file = t_name + '-extracted' + t_ext
        debug(stn_file)
        debug(extr_file)

        addStnFile = find(stn_file, f)
        addExtrFile = find(extr_file, f)
        debug(addStnFile)
        debug(addExtrFile)
        if addStnFile is not None:
            debug("Adding file")
            all_star_html.append(addStnFile)
        if addExtrFile is not None:
            debug("Adding -extracted file")
            all_star_html.append(addExtrFile)
    return all_star_html


def get_all_tags_text(pt):
    """
    Get all text from inner tags.

    *pt* parent tag
    """
    all_tags_text = []
    for tag in pt.contents:
        if isinstance(tag, bs4.element.NavigableString):
            all_tags_text.append({'str': str(tag), 'tag': tag})
    return all_tags_text


def generate_new_html_for_words(words):
    """
    Go through list of words, and generates the HTML + Ruby characters.

    *words* a list of chinese words
    """
    words_with_pinyin_html = ""

    for word in words:
        debug("{0} : {1}".format(word, "".join(words)))
        debug('CHARACTER: {0}'.format(word))
        if not is_entirely_chinese(word):
            pi = (' '*len(word)).split(' ')
        else:
            zh = hanzi.to_zhuyin(word)
            debug('ZHUYIN: {0}'.format(zh))
            pi = trans.zhuyin_to_pinyin(
                zh,
                accented=not numbered_pinyin).split(' ')
            debug('PINYIN: {0}'.format(pi))
        debug("{0}={1}".format(word, "".join(pi)))
        words_with_pinyin_html += html.to_html(word, top=pi, minified=True)

    return words_with_pinyin_html


def add_js_link(bs_file):
    """
    Return file w/ link to js/functions.js file.

    *bs_file* Beautiful Soup file object.
    """
    js_link = bs_file.new_tag("script", type="text/javascript", src="./js/functions.js")
    bs_file.head.insert(-1, js_link)
    return bs_file


def get_pinyin_bs(file_name):
    """
    Return file + Ruby characters.

    *fn* file name to run on
    """
    # open file and parse with bs4, with xml rules
    debug(file_name)
    f = open(file_name, 'r')
    s1 = f.read()
    f.close()
    bs = BeautifulSoup(s1, 'xml')

    # Go through all the 'text' tags and extract only the tags' strings
    # assign to all_of_the_tags
    all_of_the_tags = []

    for tn in GET_TAG_NAMES:
        for t in bs.findAll(tn):
            if "href" in t:
                t['href'] = htmlLib.escape(t['href'])
            for ts in get_all_tags_text(t):
                all_of_the_tags.append(ts)

    for p in all_of_the_tags:
        debug(p)
        p_el = p['tag']
        p_text = p['str']
        debug(p_text)
        new_p_str = ''

        debug('WORKING ON: ')
        debug("#######{0}#######".format(p_text))
        # pos_tagging will give you the type of word
        # unneccesary in this case
        words = [word for word in jieba.cut(p_text)]
        debug("WORDS: {0}".format(words))
        new_p_str = generate_new_html_for_words(words)
        debug("Parent Element: " + str(p_el.parent))
        debug("{0} will be replaced by {1}".format(p_el, new_p_str))
        p_el.replace_with(bs.new_string(new_p_str))
    return str(add_js_link(bs).decode(formatter=None))


files = find_epub_files(FILE_NAME)
debug(files)
jieba.load_userdict(dict_file)
total_files = 0
current_file_num = 1
for fn in files:
    total_files += 1

for fn in files:
    if fn != "":
        print("{0}({1})/{2} starting... ".format(
            current_file_num,
            fn,
            total_files))
        new_text = get_pinyin_bs(fn)
        debug(new_text)
        new_f = open("{0}/{1}".format(NEW_DIR, fn), encoding='utf-8', mode='w')
        new_f.write(new_text)
        new_f.close()
        current_file_num += 1
