# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'docs'
copyright = '2023, Mekstack'

version = '9999'
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
html_static_path = ['images', 'files']

# -- Options for HTML output
html_theme = 'openstackdocs'
