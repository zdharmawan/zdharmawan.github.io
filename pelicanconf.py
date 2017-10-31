#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Zul Dharmawan'
SITENAME = u'Zul Dharmawan'
SITEURL = 'zdharmawan.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/zdharmawan'),
          ('Github', 'https://github.com/zdharmawan'),)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = '/Users/310176470/Personal/github/pelican-themes/pelican-sober'

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['/Users/310176470/Personal/github/zdharmawan.github.io/plugins']
PLUGINS = ['ipynb.markup']
