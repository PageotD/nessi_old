#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from Cython.Build import cythonize
import numpy
import io
import os
import sys

# Package meta-data.
NAME = 'NeSSI'
DESCRIPTION = 'NeSSI for rapid development of seismic inversion codes.'
URL = 'https://framagit.org/PageotD/nessi/'
EMAIL = 'damien.pageot@protonmail.com'
AUTHOR = 'Damien Pageot'
REQUIRES_PYTHON = '>=3.0'
VERSION = '0.3.0'

# Packages are required for NeSSI to be executed
#REQUIRED = [
#    'cython', 'numpy', 'scipy', 'matplotlib',
#]

# Optional packages
EXTRAS = {}

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name=NAME,
    version=VERSION,

    # Meta-data informations
    author=AUTHOR,
    author_email=EMAIL,
    license="LGPL3",
    keywords="near surface seismic imaging",
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(),

    #install_requires=REQUIRED,
    #extras_require=EXTRAS,
    include_package_data=True,

    # Required packages
    #setup_requires=['cython'],

    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Cython',
        ],

    # Cythonize
    ext_modules = cythonize(["nessi/modbuilder/*.pyx",
                             "nessi/modeling/swm/*.pyx",
                             "nessi/signal/dsp/*.pyx",
                             "nessi/misc/source_estimation/*.pyx"],
                             compiler_directives={'language_level' : "3"}),
    include_dirs = [numpy.get_include()],

)
