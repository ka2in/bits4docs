# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))


# -- Project information -----------------------------------------------------

project = 'bits4docs'
copyright = '2025, GlobalTech Translations'
author = 'GlobalTech Translations'


# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config
from docutils.parsers.rst import Directive

import sphinxemoji

import pydata_sphinx_theme


extensions = [
    'myst_parser',
	'sphinx_rtd_theme',
    'sphinx.ext.autosectionlabel',
    'sphinx_markdown_tables',
    'sphinxcontrib.inkscapeconverter',
    'sphinxcontrib.httpdomain',
    'sphinxemoji.sphinxemoji',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

<<<<<<< HEAD
=======
# Setting a consistent emoji style

sphinxemoji_style = 'twemoji'

>>>>>>> easydocbranch
# Settings for sphinx-markdown-tables

source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}

source_suffix = ['.rst', '.md']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = "pydata_sphinx_theme"

# -- Adding options for TOC ------------------------------------------------

html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/ka2in",
            "icon": "fab fa-github-square",
            "type": "fontawesome",
        },
        {
            "name": "Mastodon",
            "url": "https://fosstodon.org/@gnufcl",
            "icon": "fab fa-mastodon",
            "type": "fontawesome",
        },
   ],
    "navbar_start": "navbar-logo",
    "pygment_light_style": "tango",
    "pygment_dark_style": "native",
    "footer_start": "copyright",
    "footer_end": "",
    'collapse_navigation': True, # ToC options - Collapse empty navigation sections
    "show_nav_level": 2, # Adjust this value as needed
    "navigation_depth": 4,  # Adjust this value as needed
}

html_sidebars = {
    "**": ["search-field.html"]
}


# Dark mode as default

html_context = {
   "default_mode": "dark",
}

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Adding settings for custom css file in the _Static folder
def setup(app):
  app.add_css_file('css/custom.css')

#Disable the option 'View page source' on the homepage

html_show_sourcelink = False

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.

html_logo = "drawing-icon.png"


# LaTeX customization for PDF 

latex_engine = 'xelatex'

latex_elements = {
    'fontpkg': r'''
\\usepackage{fontspec}
\setmainfont{Symbole}
''',
    'preamble': r'''
\usepackage[titles]{tocloft}
\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
\setlength{\cftchapnumwidth}{0.75cm}
\setlength{\cftsecindent}{\cftchapnumwidth}
\setlength{\cftsecnumwidth}{1.25cm}
''',
}

latex_show_urls = 'footnote'

# Grouping the document tree into LaTeX files. List of tuples# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
 ('index', 'yourdoc.tex', u'bits4docs Documentation', u'GlobalTech Translations', 'manual'),
 ]

# Options for LaTeX output
latex_elements = {
  'extraclassoptions': 'openany,oneside',
  'fncychap' : r'\usepackage[Bjornstrup]{fncychap}',
  'printindex': r'\footnotesize\raggedright\printindex',
  'geometry': r'\usepackage{geometry}',
  'preamble': r'\usepackage[bottom]{footmisc}',

# Paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',

# Latex figure (float) alignment
    'figure_align': 'H',
}