# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from setuptools import setup

try:
    with open('README.rst') as f:
        readme = f.read()
except IOError:
    readme = ''

setup(
    name="Flask-PyMemcache",
    version='0.0.3',
    py_modules=['flask_pymemcache'],
    author='INADA Naoki',
    author_email='songofacandy at gmail dot com',
    url='https://github.com/KLab/Flask-PyMemcache',
    description="pymemcache integration for Flask",
    long_description=readme,
    install_requires=["Flask", "pymemcache>=1.2.2", "six"],
)
