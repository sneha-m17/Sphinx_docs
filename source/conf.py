# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SAS2PY'
# copyright = '2025, vishnu'
# author = 'vishnu'
release = 'V3.1.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_design",
    'sphinx_togglebutton',
    'sphinx_design',
    "myst_parser",

]


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
# html_js_files = ["sidebar-persist.js"]
html_css_files = [
    'custom.css',
    'access_login.css',
    'darktheme.css',
    'edge_image.css',
    'dark_theme_cards.css',
    'sidebar_scroll.css',
]
html_js_files = ["furo_sidebar_fix.js"]


# def setup(app):
#     app.add_css_file('border.css')
html_logo = "_static/logo.webp"

# Optional: Adjust theme-specific options if needed
html_theme_options = {
    "light_logo": "logo.webp", 
    "navigation_with_keys": True, # If you have a light version
}

html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/navigation.html",
    ],
}