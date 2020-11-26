#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------
# Filename: srcest.pyx
#   Author: Damien Pageot
#    Email: nessi.develop@protonmail.com
#
# Copyright (C) 2019 Damien Pageot
# ------------------------------------------------------------------

"""
Linear source inversion
"""

import numpy as np
cimport numpy as np
cimport cython

ctypedef np.int16_t DTYPE_i
ctypedef np.float32_t DTYPE_f
ctypedef np.complex64_t DTYPE_c

@cython.boundscheck(False)
@cython.wraparound(False)

def csrcest(np.ndarray[DTYPE_f, ndim=2] dcal, np.ndarray[DTYPE_f, ndim=1] dsrc, np.ndarray[DTYPE_f, ndim=2] dobs):
    """
    Linear source inversion for multitrace and single precision

    :param dcal: calculated data
    :param dsrc: source used for numerical data
    :param dobs: observed data
    """

    cdef Py_ssize_t ir, iw

    # Get the dimensions
    cdef int nr = np.size(dcal, axis=0)
    cdef int ns = np.size(dcal, axis=1)

    # Fast Fourier transform
    cdef np.ndarray[DTYPE_c, ndim=2] gcal = np.fft.rfft(dcal, axis=1)
    cdef np.ndarray[DTYPE_c, ndim=2] gobs = np.fft.rfft(dobs, axis=1)
    cdef np.ndarray[DTYPE_c, ndim=1] gsrc = np.fft.rfft(dsrc)

    # Prepare
    cdef nfft = len(gsrc)
    cdef np.ndarray[DTYPE_c, ndim=1] num = np.zeros(nfft, dtype=np.complex64)
    cdef np.ndarray[DTYPE_c, ndim=1] den = np.zeros(nfft, dtype=np.complex64)

    # Process
    for iw in range(0, nfft):
        for ir in range(0, nr):
            num[iw] = num[iw]+gcal[ir, iw]*np.conj(gobs[ir, iw])
            den[iw] = den[iw]+gcal[ir, iw]*np.conj(gcal[ir, iw])

    # Estimated source
    cdef np.ndarray[DTYPE_c, ndim=1] gsinv = np.zeros(nfft, dtype=np.complex64)
    cdef np.ndarray[DTYPE_c, ndim=1] gcorrector = np.zeros(nfft, dtype=np.complex64)
    for iw in range(0, nfft):
        if den[iw] != complex(0., 0.):
            gsinv[iw] = gsrc[iw]*np.conj(num[iw]/den[iw])
            gcorrector[iw] = num[iw]/den[iw]

    cdef np.ndarray[DTYPE_f, ndim=1] dsinv = np.fft.irfft(gsinv, n=ns)

    return dsinv, gcorrector
