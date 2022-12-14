# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Mekstack'
copyright = '2022, Mekstack'

version = 'preprod'
openstackdocs_auto_version = False

# -- General configuration

extensions = [
    'openstackdocstheme',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
]

templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'openstackdocs'
