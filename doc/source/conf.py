# -*- coding: utf-8 -*-

from os.path import dirname
import sys
sys.path.insert(0, dirname(dirname(dirname(__file__))))

# -- General configuration ------------------------------------------------
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.autodoc',
]
templates_path = []  # ['_templates']
source_suffix = '.rst'
master_doc = 'index'

# General information about the project.
project = u'orgparse'
copyright = u'2012, Takafumi Arakaki'

# The short X.Y version.
version = '0.0.0'
# The full version, including alpha/beta/rc tags.
release = '0.0.0'

exclude_patterns = []

pygments_style = 'sphinx'


# -- Options for HTML output
html_theme = 'default'
html_static_path = []  # ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = 'orgparsedoc'


# -- Options for LaTeX output ---------------------------------------------
latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'orgparse.tex', u'orgparse Documentation',
   u'Takafumi Arakaki', 'manual'),
]


# -- Options for manual page output ---------------------------------------
# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'orgparse', u'orgparse Documentation',
     [u'Takafumi Arakaki'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------
# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'orgparse', u'orgparse Documentation',
   u'Takafumi Arakaki', 'orgparse', 'One line description of project.',
   'Miscellaneous'),
]