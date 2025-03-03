import re
import time

extensions=['sphinx.ext.mathjax',
            'sphinx.ext.autosectionlabel',
            'sphinxcontrib.bibtex',
            'sphinxcontrib.contentui',
            'fluiddoc.mathmacro',
            'sphinxcontrib.youtube',
            'sphinx_subfigure',
            'sphinx_toolbox.collapse'
            ]

language  = 'en'
project   = 'Speakerbench'
copyright = '2020-'+time.strftime("%Y")+' | C. Futtrup and J. Candy'
author    = 'Speakerbench Team'

version = "0.1"
release = version

bibtex_bibfiles = ['refs.bib']
bibtex_default_style = 'alpha'
numfig = True

master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path    = ['_templates']
html_static_path  = ['_static']
html_css_files    = ['css/custom.css']
imgmath_font_size ='16'

# Options for HTML output

html_theme           = 'sphinx_rtd_theme'
html_favicon         = 'images/logo/favicon.ico'
html_show_sphinx     = True
html_show_copyright  = True
html_last_updated_fmt = '%b %d, %Y'

html_theme_options = {'analytics_id': '',
                      'logo_only': False,
                      'prev_next_buttons_location': 'bottom',
                      'collapse_navigation': True,
                      'sticky_navigation': True,
                      'navigation_depth': 4,
                      'includehidden': True,
                      'titles_only': False
                      }

mathjax3_config = {'tex':{'macros':{}}} # Create empty

# Entering math macros in mathjax
with open('mathmacros.tex','r') as f:
    for line in f:
        if line[0] == '\\':
            macro = re.findall(r'\\newcommand{\\(.*?)}(\[(\d)\])?{(.+)}',line)[0]
            if len(macro[1]) == 0:
                mathjax3_config['tex']['macros'][macro[0]] = "{"+macro[3]+"}"
            else:
                mathjax3_config['tex']['macros'][macro[0]] = ["{"+macro[3]+"}", int(macro[2])]
