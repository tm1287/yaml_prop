# yaml_prop
Extended `PyYAML` loader and dumper for properties with physical units used in scientific computing.

This utility extends `PyYAML` with the following `YAML` tags:
- `!array`: Takes a `yaml.SequenceNode` and converts it into the array or tensor object of your preference with `array_yaml_constructor`. The default array constructor is `numpy.array`.
- `!numexpr`: Leverages the [`numexpr` library](https://github.com/pydata/numexpr) to evaluate `numpy` expressions from a `YAML` mapping node with an `expr` node and an optional `alias` node for resolving aliases within the expression.
- `!lambda`: Creates a `python` `lambda` expression via `numexpr` from a `YAML` mapping node with `args`, `expr`, and `alias` nodes.

These basic utilities are then used to define physical properties with physical unit conversions handled by [`pint`](https://github.com/hgrecco/pint):
- `!constant`: Creates a constant physical property
- `!table`: Creates a lookup table physical property based on an underlying [`scipy.interpolate.RegularGridInterpolator`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.RegularGridInterpolator.html)
- `!function`: Wraps around a `Lambda` object and performs unit conversions.


Copyright (c) 2024-, The University of Texas at Austin

All Rights reserved.
See file COPYRIGHT for details.

This file is part of the yaml_prop package. For more information see
https://github.com/bechrist/yaml_prop

yaml_prop is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License (as published by the Free Software Foundation) version 3.0 dated June 2007.
