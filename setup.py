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
    description="pymemcache integration for Flask",
    long_description=readme,
    install_requires=["Flask", "pymemcache>=1.2.1"],
)
