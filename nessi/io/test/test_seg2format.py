#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------
# Filename: test_stream_main.py
#   Author: Damien Pageot
#    Email: nessi.develop@protonmail.com
#
# Copyright (C) 2019 Damien Pageot
# ------------------------------------------------------------------
"""
Test suite for the main methods of the Stream class.

:copyright:
    Damien Pageot (nessi.develop@protonmail.com)
:license:
    GNU Lesser General Public License, Version 3
    (https://www.gnu.org/copyleft/lesser.html)
"""

import numpy as np
from nessi.io import seg2read
import matplotlib.pyplot as plt

# Read the Seismic Unix test file
sdata = seg2read('data/nessi_test_dataB.seg2')

# Correcting trace headers (receiver position)
for i in range(0, sdata.ntrac):
    scale = sdata.header[0]['scalco']
    sdata.header[i]['sx'] = -10
    sdata.header[i]['gx'] = int(float(i)*-scale)
    sdata.header[i]['scalco'] = int(scale)

sdata.wiggle(xcur=1.0, tracewidth=1)
#sdata.image(cmap='gray')
plt.show()

# MASW
sdata.masw(vmin=500., vmax=10000., dv=250., fmin=1000., fmax=100000., whitening=True)
sdata.image(cmap='jet')
plt.show()
