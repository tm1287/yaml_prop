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
__all__ = ['PropertyLoader', 'load', 'load_all', 
           'PropertyDumper']

import numpy as np
import typing as typ
import yaml
import yaml_include

from .math import (array_yaml_constructor, numpy_array_yaml_representer,
                   numexpr_yaml_constructor, Lambda)
from .properties import ConstantProperty, TableProperty, FunctionProperty


# %%
_IncludeConstructors = yaml_include.Constructor | dict[str, yaml_include.Constructor]


class PropertyLoader(yaml.SafeLoader):
    include_constructor: _IncludeConstructors | None = None

    def __init__(self,
            stream, #: yaml._ReadStream
    ):
        super().__init__(stream)
        
        for prop in (ConstantProperty, TableProperty, FunctionProperty):
            self.add_constructor(prop._yaml_tag, prop.yaml_constructor)

        self.add_constructor(u'!array', array_yaml_constructor)
        self.add_constructor(u'!numexpr', numexpr_yaml_constructor)
        self.add_constructor(Lambda._yaml_tag, Lambda.yaml_constructor)

        """Invoke default constructor if :code:`set_include_constructor` was not called prior to :code:`PropertyLoader` instantiation"""
        if self.include_constructor is None:
            self.include_constructor = yaml_include.Constructor()

        if isinstance(self.include_constructor, dict):
            for tag, constr in self.include_constructor.items():
                self.add_constructor(f"!include_{tag}", constr)
        else:
            self.add_constructor("!include", self.include_constructor)

    @staticmethod
    def set_include_constructor(include_constructor: _IncludeConstructors):
        """Singleton pattern for setting :code:`include_constructor`"""
        if PropertyLoader.include_constructor is None:
            PropertyLoader.include_constructor = include_constructor

def load(stream) -> dict:
    """Thin wrapper of :code:`yaml.load()` with a :code:`PropertyLoader`"""
    return yaml.load(stream, Loader=PropertyLoader)


def load_all(stream) -> typ.Generator[dict, None, None]:
    """Thin wrapper of :code:`yaml.load_all()` with a :code:`PropertyLoader`"""
    return yaml.load_all(stream, Loader=PropertyLoader)


# %%
class PropertyDumper(yaml.SafeDumper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for prop in (ConstantProperty, TableProperty, FunctionProperty):
            self.add_representer(prop, prop.yaml_representer)

        self.add_representer(type(None), lambda dumper, _: dumper.represent_scalar(u'tag:yaml.org,2002:null', ''))
        self.add_representer(np.ndarray, numpy_array_yaml_representer)
        self.add_representer(Lambda, Lambda.yaml_representer)
