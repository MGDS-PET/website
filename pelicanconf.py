#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'OCAD University'
SITENAME = u'MGDS-PET Wearables'
#SITEURL = 'https://github.com/MGDS-PET/mgds-pet.github.io'
TIMEZONE = 'America/Toronto'
DEFAULT_LANG = u'en'
#GITHUB_URL = 'http://github.com/ametaireau/'

# custom page generated with a jinja2 template
#TEMPLATE_PAGES = {'pages/jinja2_template.html': 'jinja2_template.html'}
#TAGS_SAVE_AS = ''
#TAG_SAVE_AS = ''

PATH = 'content'
#dynamic content = 'articles'
ARTICLE_PATHS = ['articles/blog', 'articles/components', 'articles/devices', 'articles/ideas', 'articles/team']
USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = True
FAVICON = 'images/favicon.ico'
#SITELOGO = 'images/favicon.ico'
PDF_GENERATOR = True
PLUGIN_PATHS = ["plugins", "/plugins"]
PLUGINS = ["pdf"] #, "liquid_tags", "sitemap"]

#static content = 'pages'
STATIC_PATHS = ['pages', 'pdfs', 'images'] # 'downloads']

# EXTRA_PATH_METADATA = {
#     'extra/favicon.ico': {'path': 'favicon.ico'}
# }

DISPLAY_PAGES_ON_MENU = False
DISPLAY_BREADCRUMBS = True
#DISPLAY_ARTICLE_INFO_ON_INDEX = True

MENUITEMS = [
#('Home', '/'), #necessary? Redundant
]
    
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{slug}.html'
ARTICLE_URL = 'articles/{date:%Y}/{slug}.html'
DEFAULT_DATE = 'fs'
TYPOGRIFY = True
THEME = 'themes/bootstrap' 
BOOTSTRAP_THEME = 'yeti' #others available 'cosmo' etc. all included already. See http://bootswatch.com/
#BANNER = 'images/bluePlanet.png'
#BANNER_SUBTITLE = 'Banner subtitle'
#BANNER_ALL_PAGES = True

DEFAULT_PAGINATION = False
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
#LOAD_CONTENT_CACHE = False # avoids caching of content during development

# Social widget
SOCIAL = (
('Google+ Images', '#'),
('SoundCloud Adam', 'https://soundcloud.com/adamtindale'),
)

# Blogroll
LINKS = (
('OCADU University', 'http://www.ocadu.ca/'),
('DFI@OCADU', 'http://www.ocadu.ca/academics/faculty-of-las-and-sis/digital-futures-initiative.htm'),
('Adam Tindale', 'adamtindale.com'),
('Rhizome', 'http://rhizome.org/'),
)
