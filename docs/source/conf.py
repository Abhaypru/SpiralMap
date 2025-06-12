# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
from pathlib import Path
sys.path.insert(0, os.path.abspath('../../src'))

project = 'SpiralMap'
copyright = '2025, Abhay Kumar Prusty & Shourya Khanna'
author = 'Prusty & Khanna'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.mathjax",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode"
]
templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_baseurl = "https://spiralmap.readthedocs.io/en/latest/"

# -- Google Analytics (GA4) integration --------------------------------------

def setup(app):
    app.add_js_file("https://www.googletagmanager.com/gtag/js?id=G-2D1BGW81C9")
    app.add_js_file(None, body="""
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-2D1BGW81C9');
    """)
