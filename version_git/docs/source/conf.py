'''SPHINX Configuration File.'''
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
from pathlib import Path
import sys
# sys.path.insert(0, os.path.abspath('../..'))
sys.path.insert(0, str(Path('..','..').resolve()))
# pylint: disable=import-error
import setup_version  # type: ignore

# -- Project information -----------------------------------------------------

# We would really want this read from pyproject.toml in the future.
# pylint: disable=invalid-name
project = "Program Version from Git Describe"

# No real way to keep this automatically up to date.
# pylint: disable=invalid-name, redefined-builtin
copyright = 'Copyright 2021-2025 John. E. Malmberg'

# This should also come from pyproject.toml
# pylint: disable=invalid-name
author = 'John. E. Malmberg WB8TYW'

# pylint: disable=invalid-name
release = setup_version.SETUP_VERSION

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary']

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
# pylint: disable=invalid-name
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
