# -*- coding: utf-8 -*-

import os
import sys
import defusedxml.ElementTree

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.viewcode',
    'sphinxarg.ext'
]

# This invocation turns on documenting class constructors (off by default)
autoclass_content = 'both'

source_suffix = '.rst'
master_doc = 'index'

project = u'robot_upstart'
copyright = u'2015, Mike Purvis'

# Get version number from package.xml.
tree = defusedxml.ElementTree.parse('../package.xml')
version = tree.find("version").text
release = version

html_theme = 'nature'
htmlhelp_basename = 'robot_upstartdoc'
