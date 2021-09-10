# -*- coding: utf-8 -*-

import sys

import requests
from htmltext import HTMLText

if __name__ == '__main__':
    """
    """
    if len(sys.argv) < 2:
        print("Usage: python %s article_url" % __file__)
    else:
        r = requests.get(sys.argv[1])
        title, text = HTMLText(r.content)
        print(title)
        print(text)
            
