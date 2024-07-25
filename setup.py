"""Extended PyYAML Property Loader and Dumper

Copyright (c) 2024-, The University of Texas at Austin

All Rights reserved.
See file COPYRIGHT for details.

This file is part of the yaml_prop package. For more information see
https://github.com/bechrist/yaml_prop

yaml_prop is free software; you can redistribute it and/or modify it under the
terms of the GNU General Public License (as published by the Free
Software Foundation) version 3.0 dated June 2007.
"""
__authors__ = ['Blake Christierson, UT Austin <bechristierson@utexas.edu>']

import os

from setuptools import setup, find_packages


# %%
PROJ_DIR = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(PROJ_DIR, 'README.md'), encoding='utf-8') as file:
    LONG_DESCRIPTION = file.read()

REQUIREMENTS = [
    'matplotlib',
    'numpy',
    'scipy',
    'pyyaml',
    'numexpr',
    'pint',
    'mip'
]

KEYWORDS = """
    YAML,
    I/O,
    Physical Properties"""

setup(
    name = 'yaml_prop',
    version = '0.0.1',
    description = 'yaml_prop - PyYAML extension for property configuration files',
    long_description = LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url = 'https://github.com/bechrist/yaml_prop',
    author = 'Blake Christierson', 
    author_email = 'bechristierson@utexas.edu',
    packages=find_packages(exclude=['examples', 'doc', 'test']),
    install_requires=REQUIREMENTS)