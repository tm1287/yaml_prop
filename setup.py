from setuptools import setup

setup(
    name = 'yaml_prop',
    version = '0.0.1',
    description = 'yaml_prop - PyYAML extension for property configuration files',
    author = "Blake Christierson", 
    author_email = ['bechristierson@utexas.edu'],
    url = 'https://github.com/bechrist/yaml_prop',
    long_description = """
    Extended PyYAML loader and dumper for phyiscal properties used in scientific computing.

    Copyright (c) 2024-, The University of Texas at Austin

    All Rights reserved.
    See file COPYRIGHT for details.

    This file is part of the yaml_prop package. For more information see https://github.com/bechrist/yaml_prop

    yaml_prop is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License (as published by the Free Software Foundation) version 3.0 dated June 2007.
    """,
    packages=['package'])