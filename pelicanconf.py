#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Calvin Spealman'
SITENAME = 'www.ironfroggy.com'
SITEURL = 'http://localhost:8000'

PATH = 'content'
THEME = 'theme'
THEME_STATIC_DIR = 'static'
STATIC_PATHS = ['images']

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

CATEGORY_SAVE_AS = CATEGORY_URL = "{slug}/index.html"
ARTICLE_SAVE_AS = ARTICLE_URL = "{category}/{date:%Y}/{slug}.html"
TAGS_SAVE_AS = "tag/index.html"

# Blogroll
LINKS = (
    #('Pelican', 'http://getpelican.com/'),
)

# Social widget
SOCIAL = (
    ('@ironfroggy', 'http://twitter.com/ironfroggy/'),
    ('Github', 'http://github.com/ironfroggy'),
    ('My Web Have-Read List', 'http://ironfroggy-reads.tumblr.com/'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = False

MENUITEMS = (
    ("About", "/pages/about.html"),
    ("Tags", "/tag/"),
)
