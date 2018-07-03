#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'authorname'
SITENAME = "CMSE Pelican/Github.io tutorial"
SITEURL = ''
PATH = 'content'


# Following items are often useful when publishinu
#DISQUS_SITENAME = "DISQUS SITE NAME"
#GOOGLE_ANALYTICS = "UA-XXXXXXXXX-X"


#PLUGIN_PATHS=["./plugins"]
#PLUGINS=['ipynb.markup']
#MARKUP = { 'md', 'ipynb'}

TIMEZONE = 'America/Detroit'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('CMSE', 'http://cmse.msu.edu'),
         ('MSU', 'http://www.msu.edu/'))

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Comment following line if you want the default theme
THEME = 'themes/tuxlite2'

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

#INDEX_SAVE_AS = 'about.html'
#PAGE_SAVE_AS = 'about2.html'
#PAGE_URL = 'about2.html'

# Provides menu items, which come before pages / categories
#MENUITEMS = [('News','file:///Users/cmse/Desktop/pelican/backupblog/output/category/#news.html')]
