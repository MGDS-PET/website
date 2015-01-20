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

DISPLAY_BREADCRUMBS = True
#DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True

#dynamic content = 'articles'
#ARTICLE_PATHS = ['articles/components', 'articles/devices', 'articles/ideas', 'articles/team']
USE_FOLDER_AS_CATEGORY = True #eg. 'blog'
DISPLAY_CATEGORIES_ON_MENU = False
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{slug}.html' #must be same as article_url below
ARTICLE_URL = 'articles/{date:%Y}/{slug}.html'
#SLUGIFY_SOURCE = 'title' #use title field
#SLUGIFY_SOURCE = 'basename' #use file name

#static content = 'pages'
STATIC_PATHS = ['pages', 'pdfs', 'images', 'extra/custom.css'] # 'downloads']
DISPLAY_PAGES_ON_MENU = False
FAVICON = 'images/_site/favicon.ico'
PAGE_SAVE_AS = 'pages/{slug}.html' #must be same as page_url below
PAGE_URL = 'pages/{slug}.html' 	#The URL we will use to link to a page.

MENUITEMS = [
#('Home', '/'), #not needed
#mixing dynamic and static content in menu:
	('Blog', '/category/blog.html'), #dynamic = articles
	('Components', '/pages/components/components.html'), #static = pages
	('Devices', '/pages/devices/devices.html'),
	('Ideas', '/pages/ideas/ideas.html'),
	('Team', '/pages/team/team.html')
]  

#SITELOGO = 'images/favicon.ico'
#PDF_GENERATOR = False #output goes to output/pdf
PLUGIN_PATHS = ["plugins", "/plugins"]
#PLUGINS = ["pdf"] #, "liquid_tags", "sitemap"]

DEFAULT_DATE = 'fs'
TYPOGRIFY = True
THEME = 'themes/bootstrap' 
BOOTSTRAP_THEME = 'yeti' #others available 'cosmo' etc. all included already. See http://bootswatch.com/
CUSTOM_CSS = 'theme/css/custom.css' #where Pelican should put the custom css file

# Tell Pelican to change the path to 'theme/css/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'theme/css/custom.css'}
}
 #load this file in addition to the css files in the bootstrap theme
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
