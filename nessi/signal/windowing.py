#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------
# Filename: tapering.py
#   Author: Damien Pageot
#    Email: nessi.develop@protonmail.com
#
# Copyright (C) 2018, 2019 Damien Pageot
# ------------------------------------------------------------------
"""
Data windowing functions.

:copyright:
    Damien Pageot (nessi.develop@protonmail.com)
:license:
    GNU Lesser General Public License, Version 3
    (https://www.gnu.org/copyleft/lesser.html)
"""

import numpy as np

def timeWindow(data, dt, delay, tmin, tmax):
    """
    """

    # Get the number of samples
    ns = len(data)

    # Get data lenght
    dataLenght = float(ns-1)*dt

    # Get start and end time
    startTime = -1.*delay
    endTime = startTime+dataLenght

    # Get start and end index
    startIndex = int((tmin+delay)/dt)
    endIndex = int((tmax+delay)/dt)

    return data[startIndex:endIndex+1]
