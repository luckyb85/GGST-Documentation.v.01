# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Trials///'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    #'sphinx_rtd_size',
    'sphinx.ext.intersphinx',
]

#sphinx_rtd_size_width = "90%"

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
    
def setup(app):
    app.add_css_file('my_theme.css')
html_static_path = ['_statics']



def setup(app):
    app.add_css_file('css/custom.css')  # may also be an URL
