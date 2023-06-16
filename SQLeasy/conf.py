# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# If the extensions (or mudules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here:
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import os, sys
sys.path.insert(0, os.path.abspath('.'))

# The encoding of source filenames
#
source_encoding ='utf-8-sig'

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = 'SphinxDocs'
copyright = '2023, Raul Vilchez'
author = 'Raul Vilchez'
release = '1.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.duration',
              'sphinx.ext.autosummary'
             ]
              # sphinx.ext.intersphinx # to link external documentation.
                                       # The var intersphinx_mapping should be
                                       # initialized too.
              # sphinx.ext.doctest     # Code snippets in the documentation.
                                       # It's used as a simmple unitTest tool.

templates_path = ['_templates']
exclude_patterns = []

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['rst', 'md']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# To use other thems, install the extension first, and then replace the used
# one, by the new you just had installed; i.e: html_theme = 'my_new_theme'

html_theme = 'alabaster'
html_static_path = ['_static']
# intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}
