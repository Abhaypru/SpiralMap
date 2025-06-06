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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "SpiralMap"
copyright = "2025, SpiralMap"
author = "Prusty & Khanna"
release = "0.1.0"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx_automodapi.automodapi",
    "sphinx.ext.napoleon",
    "matplotlib.sphinxext.plot_directive",
    "sphinx_copybutton",
    "myst_nb",
]

extensions.append('sphinxcontrib.bibtex')
bibtex_bibfiles = ['refs.bib']
bibtex_reference_style = "author_year"
bibtex_default_style = 'latin'

numpydoc_show_class_members = False

# myst_nb configurations
source_suffix = {
    ".rst": "restructuredtext",
    ".ipynb": "myst-nb",
    ".myst": "myst-nb",
}
nb_execution_mode = "off"
myst_enable_extensions = ["dollarmath"]
# auto-generate heading anchors down to this level
myst_heading_anchors = 3

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# hide input prompts in notebooks
nbsphinx_prompt_width = "0"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
##
html_theme = "sphinx_book_theme"
html_theme_options = {
    "path_to_docs": "docs",
    "repository_url": "https://github.com/Abhaypru/SpiralMap",
    "repository_branch": "main",
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "colab_url": "https://colab.research.google.com/",
        "notebook_interface": "jupyterlab",
    },
    "use_edit_page_button": False,
    "use_issues_button": True,
    "use_repository_button": True,
    "use_download_button": True,
	"navbar_end": ["navbar-icon-links"],    
    "default_mode": "light"
}
html_baseurl = "https://spiralmap.readthedocs.io/en/latest/"


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# hide coppy button on outputs
copybutton_selector = "div:not(.output) > div.highlight pre"
