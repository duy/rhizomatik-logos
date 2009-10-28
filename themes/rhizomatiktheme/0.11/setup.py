#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from setuptools import setup

setup(
    name = 'TracRhizomatikTheme',
    version = '1.0',
    packages = ['rhizomatiktheme'],
    package_data = { 'rhizomatiktheme': ['templates/*.html', 'htdocs/*.png', 'htdocs/*.css', 'htdocs/img/*.gif', 'htdocs/img/*.jpg' ] },

    author = 'duy',
    author_email = 'duy@rhizomatik.net',
    description = 'Rhizomatik Labs Trac theme',
    license = 'GPL',
    keywords = 'trac plugin theme',
    url = 'http://rhizomatik.net/wiki/RhizomatikTheme',
    classifiers = [
        'Framework :: Trac',
    ],
    
    install_requires = ['Trac', 'TracThemeEngine>=2.0'],

    entry_points = {
        'trac.plugins': [
            'rhizomatiktheme.theme = rhizomatiktheme.theme',
        ]
    },
)
