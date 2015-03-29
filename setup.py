# -*- coding: utf-8 -*-
__author__ = 'DeonHeyns'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Simple project scaffolding for a Flask application',
    'author': 'Deon Heyns',
    'url': 'https://github.com/DeonHeyns/flask-generate',
    'download_url': '',
    'author_email': 'deon@deonheyns.com',
    'version': '0.0.1',
    'install_requires': ['flask'],
    'packages': ['scaffold'],
    'scripts': [],
    'name': 'Flask-Generate',
    'entry_points': {
        'console_scripts': [
            'flask-generate = scaffold.__main__:main',
        ],
        'virtualenvwrapper.project.template': [
            'base = scaffold.virtualenvwrapper:template',
        ],
    }


}

setup(**config)