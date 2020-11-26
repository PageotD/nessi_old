# -*- coding: utf-8 -*-
# -------------------------------------------------------------------
# Filename: Core
#   Author: Damien Pageot
#    Email: nessi.develop@protonmail.com
#
# Copyright (C) 2019 Damien Pageot
# ------------------------------------------------------------------
"""
Initialization file for nessi.core.

:copyright:
    Damien Pageot (nessi.develop@protonmail.com)
:license:
    GNU Lesser General Public License, Version 3
    (https://www.gnu.org/copyleft/lesser.html)
"""

# Import nessi.core classes and functions
from .stream import Stream
#from .traces import Trace
from .stream import susrcinv, susrccorr

if __name__ == '__main__':
    import doctest
    doctest.testmod(exclude_empty=True)
