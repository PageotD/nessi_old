#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------
# Filename: test_filtering.py
#   Author: Damien Pageot
#    Email: nessi.develop@protonmail.com
#
# Copyright (C) 2018, 2019 Damien Pageot
# ------------------------------------------------------------------
"""
Test suite for the filtering functions (nessi.signal.windowing)

:copyright:
    Damien Pageot (nessi.develop@protonmail.com)
:license:
    GNU Lesser General Public License, Version 3
    (https://www.gnu.org/copyleft/lesser.html)
"""

import numpy as np
from nessi.signal.filtering import getfilter
from nessi.signal.filtering import sin2filter

def test_getfilter():
    """
    signal.filtering.getfilter testing
    """

    # Create initial data trace (Dirac)
    ns = 128   # number of time sample
    dt = 0.01 # time sampling

    # Filter parameters
    freq = np.zeros(4, dtype=np.float32)
    amps = np.zeros(4, dtype=np.float32)
    freq[0] = 5.0
    freq[1] = 15.0
    freq[2] = 25.0
    freq[3] = 35.0
    amps[0] = 0.0
    amps[1] = 1.0
    amps[2] = 1.0
    amps[3] = 0.0

    # Get filter
    pfilt = getfilter(ns, dt, freq, amps)

    # Attempted output
    output = np.array([0.        , 0.        , 0.        , 0.        , 0.        , 0.        ,
                       0.        , 0.01452909, 0.05727199, 0.12574463, 0.21596763, 0.32269755,
                       0.43973166, 0.56026834, 0.6773024 , 0.78403234, 0.87425536, 0.94272804,
                       0.9854709 , 1.        , 1.        , 1.        , 1.        , 1.        ,
                       1.        , 1.        , 1.        , 1.        , 1.        , 1.        ,
                       1.        , 1.        , 1.        , 0.9829629 , 0.9330127 , 0.8535534 ,
                       0.75      , 0.62940955, 0.5       , 0.37059048, 0.25      , 0.14644662,
                       0.0669873 , 0.01703709, 0.        , 0.        , 0.        , 0.        ,
                       0.        , 0.        , 0.        , 0.        , 0.        , 0.        ,
                       0.        , 0.        , 0.        , 0.        , 0.        , 0.        ,
                       0.        , 0.        , 0.        , 0.        , 0.        ], dtype=np.float32)

    # Testing
    np.testing.assert_allclose(pfilt, output, atol=1.e-7)

def test_getfilter():
    """
    signal.filtering.getfilter testing
    """

    # Create initial data trace (Dirac)
    ns = 128   # number of time sample
    dt = 0.01 # time sampling

    # Filter parameters
    freq = np.zeros(4, dtype=np.float32)
    amps = np.zeros(4, dtype=np.float32)
    freq[0] = 5.0
    freq[1] = 15.0
    freq[2] = 25.0
    freq[3] = 35.0
    amps[0] = 0.0
    amps[1] = 1.0
    amps[2] = 1.0
    amps[3] = 0.0

    # Get filter
    pfilt = getfilter(ns, dt, freq, amps)

    # Attempted output
    output = np.array([0.        , 0.        , 0.        , 0.        , 0.        , 0.        ,
                       0.        , 0.01452909, 0.05727199, 0.12574463, 0.21596763, 0.32269755,
                       0.43973166, 0.56026834, 0.6773024 , 0.78403234, 0.87425536, 0.94272804,
                       0.9854709 , 1.        , 1.        , 1.        , 1.        , 1.        ,
                       1.        , 1.        , 1.        , 1.        , 1.        , 1.        ,
                       1.        , 1.        , 1.        , 0.9829629 , 0.9330127 , 0.8535534 ,
                       0.75      , 0.62940955, 0.5       , 0.37059048, 0.25      , 0.14644662,
                       0.0669873 , 0.01703709, 0.        , 0.        , 0.        , 0.        ,
                       0.        , 0.        , 0.        , 0.        , 0.        , 0.        ,
                       0.        , 0.        , 0.        , 0.        , 0.        , 0.        ,
                       0.        , 0.        , 0.        , 0.        , 0.        ], dtype=np.float32)

    # Testing
    np.testing.assert_allclose(pfilt, output, atol=1.e-7)

def test_sin2filter_one_trac():
    """
    signal.filtering.sin2filter testing for one trace signal.
    """

    # Create initial data trace (Dirac)
    ns = 128   # number of time sample
    dt = 0.01 # time sampling
    dobs = np.zeros((ns), dtype=np.float32)
    dobs[63] = 1.0

    # Filter parameters
    freq = np.zeros(4, dtype=np.float32)
    amps = np.zeros(4, dtype=np.float32)
    freq[0] = 5.0
    freq[1] = 10.0
    freq[2] = 20.0
    freq[3] = 25.0
    amps[0] = 0.0
    amps[1] = 1.0
    amps[2] = 1.0
    amps[3] = 0.0

    # Filtering
    dobsf = sin2filter(dobs, dt, freq=freq, amps=amps)

    # Attempted output
    output = np.array([-5.54323196e-06, -2.67922878e-05, -4.38392162e-05, -2.56523490e-05,
                       -1.25998631e-05, -5.27026132e-05, -6.59516081e-05,  3.31643969e-05,
                        1.20099634e-04,  2.98358500e-05, -1.17926858e-04, -8.66560731e-05,
                        5.73405996e-05,  7.17360526e-05, -1.60373747e-06,  6.73420727e-05,
                        2.38665845e-04,  3.01256776e-04,  2.87188042e-04,  2.93306541e-04,
                        1.25568826e-04, -2.97189690e-04, -5.27217053e-04, -2.92016659e-04,
                       -1.57086179e-04, -5.71195967e-04, -8.19603214e-04, -1.44248828e-04,
                        6.84298575e-04,  4.52522188e-04, -3.73840332e-04, -4.29369509e-04,
                        1.37770548e-04,  1.33991241e-04, -2.59846449e-04,  7.57575035e-05,
                        8.69309064e-04,  1.26846228e-03,  2.08635814e-03,  3.79829784e-03,
                        3.68275773e-03, -1.59385148e-04, -3.58604267e-03, -2.27281894e-03,
                       -1.25252269e-03, -8.08455888e-03, -1.64256226e-02, -1.13567263e-02,
                        4.59289039e-03,  9.86163318e-03, -3.32099095e-04,  9.40356404e-04,
                        2.84879040e-02,  4.81923074e-02,  2.27911919e-02, -1.91644467e-02,
                       -1.62484571e-02,  1.78811178e-02, -9.80888493e-03, -1.23780027e-01,
                       -1.91054940e-01, -6.90010190e-02,  1.76932275e-01,  3.04687500e-01,
                        1.76932275e-01, -6.90010339e-02, -1.91054940e-01, -1.23780042e-01,
                       -9.80888959e-03,  1.78811178e-02, -1.62484646e-02, -1.91644449e-02,
                        2.27911919e-02,  4.81923036e-02,  2.84879096e-02,  9.40359896e-04,
                       -3.32101248e-04,  9.86163691e-03,  4.59288619e-03, -1.13567300e-02,
                       -1.64256208e-02, -8.08456540e-03, -1.25252060e-03, -2.27281218e-03,
                       -3.58604454e-03, -1.59382820e-04,  3.68275400e-03,  3.79829435e-03,
                        2.08635814e-03,  1.26846973e-03,  8.69313255e-04,  7.57537782e-05,
                       -2.59846449e-04,  1.33987516e-04,  1.37783587e-04, -4.29376960e-04,
                       -3.73834744e-04,  4.52518463e-04,  6.84298575e-04, -1.44250691e-04,
                       -8.19604378e-04, -5.71203418e-04, -1.57091767e-04, -2.92018289e-04,
                       -5.27217053e-04, -2.97184568e-04,  1.25570223e-04,  2.93313758e-04,
                        2.87193805e-04,  3.01255845e-04,  2.38666311e-04,  6.73383474e-05,
                       -1.60234049e-06,  7.17332587e-05,  5.73272700e-05, -8.66595656e-05,
                       -1.17919873e-04,  2.98405066e-05,  1.20102428e-04,  3.31788324e-05,
                       -6.59562647e-05, -5.27063385e-05, -1.25968363e-05, -2.56616622e-05,
                       -4.38317657e-05, -2.68034637e-05, -5.54323196e-06, -7.45058060e-09], dtype=np.float32)

    # Testing
    np.testing.assert_allclose(dobsf, output, atol=1.e-7)

if __name__ == "__main__" :
    np.testing.run_module_suite()
