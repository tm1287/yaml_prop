"""Math expression evaluation

Copyright (c) 2024-, The University of Texas at Austin

All Rights reserved.
See file COPYRIGHT for details.

This file is part of the yaml_prop package. For more information see
https://github.com/bechrist/yaml_prop

yaml_prop is free software; you can redistribute it and/or modify it under the
terms of the GNU General Public License (as published by the Free
Software Foundation) version 2.0 dated June 1991.
"""
__authors__ = ['Blake Christierson, UT Austin <bechristierson@utexas.edu>']
__all__ = ['array_yaml_constructor', 'numpy_array_yaml_representer',
           'numexpr_yaml_constructor',
           'lambda_yaml_constructor', 'lambda_yaml_representer']

import typing as typ

import yaml

import numpy as np
import numexpr as ne


# %%
_Array = np.ndarray | typ.Any 
_ArrayConstructor = typ.Callable[[list], _Array]


def array_yaml_constructor(loader: yaml.Loader, node: yaml.SequenceNode,
                           constructor: _ArrayConstructor = np.array) -> _Array:
    """Constructs an array from YAML sequence(s)

    :param loader: YAML loader
    :type loader: yaml.Loader

    :param node: YAML (nested) sequence node
    :type node: yaml.SequenceNode

    :param constructor: Array constructor, defaults to :code:`numpy.array`
    :type constructor: _ArrayConstructor
    
    :return: Array
    :rtype: _Array
    """
    return constructor(loader.construct_sequence(node, deep=True))


def numpy_array_yaml_representer(dumper: yaml.Dumper, array: np.ndarray) -> yaml.SequenceNode:
    """Represents :code:`numpy.ndarray` by YAML sequence(s)

    :param dumper: YAML dumper
    :type dumper: yaml.Dumper

    :param array: :code:`numpy` Array
    :type array: numpy.ndarray

    :return: YAML (nested) sequence node
    :rtype: yaml.SequenceNode
    """
    return dumper.represent_list(array.to_list())


# %%
def numexpr_yaml_constructor(loader: yaml.Loader, node: yaml.MappingNode) -> np.ndarray:
    """Leverages :code:`numexpr` to compute :code:`numpy` expressions from YAML.

    :param loader: YAML loader
    :type loader: yaml.Loader

    :param node: YAML mapping node
    :type node: yaml.MappingNode
    
    :return: Numpy array
    :rtype: numpy.ndarray
    """
    mapping = {'expr': '', 'alias': {}}
    mapping.update(loader.construct_mapping(node, deep=True))
    return ne.evaluate(mapping['expr'], local_dict=mapping['alias'], global_dict={}) 


# %%
def lambda_yaml_constructor(loader: yaml.Loader, node: yaml.MappingNode) -> typ.Callable:
    mapping = {'args': [], 'expr': '', 'alias': {}}
    mapping.update(loader.construct_mapping(node, deep=True))
    num_args = len(mapping['args'])
    expr = ne.evaluate(mapping['expr'], local_dict=mapping['alias'])
    raise NotImplementedError


def lambda_yaml_representer(dumper: yaml.Dumper, callable: typ.Callable) -> yaml.MappingNode:
    raise NotImplementedError("Lambda YAML representer not implemented")