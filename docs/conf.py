# Copyright 2009-2022 Joshua Bronson. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# bidict documentation build configuration file, created by
# sphinx-quickstart on Fri Aug 29 11:38:22 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

"""Sphinx configuration."""

import sys
import os


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('..'))

import bidict

# -- General configuration ------------------------------------------------

# suppress_warnings = [
# ]

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    # 'sphinx.ext.coverage',
    'sphinx.ext.graphviz',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    # 'sphinx.ext.todo',
]
try:
    import sphinx_copybutton  # noqa: F401
except ImportError:
    pass
else:
    extensions.append('sphinx_copybutton')

intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}
#todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'bidict'
author = bidict.metadata.__author__['name']
copyright = bidict.metadata.__copyright__.lstrip('© ')

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
# The full version, including alpha/beta/rc tags.
release = bidict.__version__
# The short X.Y version.
version = '.'.join(release.split('.')[:2])

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'colorful'

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ['bidict.']

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'furo'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# https://pradyunsg.me/furo/customisation/#theme-options
# html_theme_options = dict(
# )

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'bidict'

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = 'bidict'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = '_static/logo-256.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# https://docs.readthedocs.io/en/stable/guides/adding-custom-css.html#adding-custom-css-or-javascript-to-sphinx-documentation
# html_css_files = ['custom.css']
html_js_files = ['custom.js']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# https://pradyunsg.me/furo/customisation/sidebar/#using-html-sidebars
html_sidebars = {
    '**': [
        'sidebar/brand.html',
        'sidebar/search.html',
        'sidebar/scroll-start.html',
        'sidebar/navigation.html',
        'sidebar/scroll-end.html',
    ],
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
html_split_index = True

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'bidictdoc'

# Ignore urls matching these regex strings when doing "make linkcheck"
linkcheck_ignore = [
    r'https://codecov\.io/.*',  # gives 405 for HEAD requests
    r'https://pypistats\.org/.*',  # unreliable
    r'https://gitpod\.io/#.*',  # linkcheck complains about anchor links on this site
    # alternative links for readers on GitHub (which don't work on readthedocs.io):
    r'docs/learning-from-bidict\.rst',
    r'CHANGELOG\.rst',
    r'docs/intro\.rst',
    r'CONTRIBUTING\.rst',
    r'CODE_OF_CONDUCT\.rst',
]
linkcheck_timeout = 10  # 5s default too low

# http://www.sphinx-doc.org/en/stable/ext/autosectionlabel.html#configuration
autosectionlabel_prefix_document = True

# https://www.sphinx-doc.org/en/3.x/usage/extensions/autodoc.html#confval-autodoc_typehints
autodoc_typehints = 'description'

# http://www.sphinx-doc.org/en/master/usage/extensions/doctest.html
doctest_global_setup = """
import sys
not_cpython = sys.implementation.name != 'cpython'
"""

# https://sphinx-copybutton.readthedocs.io/en/latest/#strip-and-configure-input-prompts-for-code-cells
copybutton_prompt_text = '>>> '
