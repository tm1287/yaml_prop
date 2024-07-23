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
__all__ = ['PropertyLoader', 'PropertyDumper']

import yaml

import numpy as np

from .math import (array_yaml_constructor, numpy_array_yaml_representer,
                   numexpr_yaml_constructor, 
                   lambda_yaml_constructor, lambda_yaml_representer)
from .properties import ConstantProperty, TableProperty, FunctionProperty


# %%
class PropertyLoader(yaml.SafeLoader):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for prop in (ConstantProperty, TableProperty, FunctionProperty):
            self.add_constructor(prop._yaml_tag, prop.yaml_constructor)

        self.add_constructor(u'!array', array_yaml_constructor)
        self.add_constructor(u'!numexpr', numexpr_yaml_constructor)
        self.add_constructor(u'!lambda', lambda_yaml_constructor)


class PropertyDumper(yaml.SafeDumper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for prop in (ConstantProperty, TableProperty, FunctionProperty):
            self.add_representer(prop, prop.yaml_representer)

        self.add_representer(np.ndarray, numpy_array_yaml_representer)
        self.add_representer(function, lambda_yaml_representer)