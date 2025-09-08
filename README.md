# Magnetic data processing pipeline

This workflow is based on work done by the DGGS (Division of Geological & Geophysical Surveys https://dggs.alaska.gov). 
The original workflow utilized Oasis Montaj and the OM python extensions. Original Author: Eric Petersen (2025-06-11).

The pipeline itself can be run either from a jupyter notebook or from
the command line using the "magproc" command line utility.

If using Jupyter notebooks, additional tools provided to plot and QC data in
various ways as well as do simple data transformations (e.g. change
coordinate projection, merge datasets, etc).

Check out the [Example](Example.ipynb) and
[gpr2025_4v2-tofty](gpr2025_4v2-tofty.ipynb) jupyter notebooks for
basic usage.

To install, simply run `pip install .`.

## Copyright

The original Oasis Montaj extension: Copyright (C) 2025 Eric Petersen
This pipeline: Copyright (C) 2025 Egil Moeller

These programs are free software: you can redistribute them and/or modify them under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. These programs are distributed in the hope that they will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details, http://www.gnu.org/licenses/.
