#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------
# Filename: suformat.py
#   Author: Damien Pageot
#    Email: nessi.develop@protonmail.com
#
# Copyright (C) 2019 Damien Pageot
# ------------------------------------------------------------------

"""
Support of seg-2 format as described by Pullan (1990).
The structure of this code is inspired by the SEG-2 file reader of the `obspy`
package (Krisher et al., 2015).

Krisher, L. et al, 2015, ObsPy: a bridge for seismology into the scientific
    Python ecosystem , Computational Science & Discovery, 8(1), 014003.
Pullan, S.E., 1990, Recommanded standard for seismic (/radar) data files in
    the personal computer environment: Geophysics, 55, 9, 1260-1271.
"""

# Import modules
import numpy as np
from nessi.core import Stream
from struct import unpack

FILE_DESCRIPTOR = {
    'ACQUISITION_DATE': '',
    'ACQUISITION_TIME': '',
    'CLIENT': '',
    'COMPANY': '',
    'GENERAL_CONSTANT': '',
    'INSTRUMENT': ['', '', ''],
    'JOB_ID': '',
    'OBSERVER': '',
    'PROCESSING_DATE': '',
    'PROCESSING_TIME': '',
    'TRACE_SORT': 'AS_ACQUIRED', # Default value
    'UNITS': 'METERS', # Default value
    'NOTE': '\n'
}

TRACE_DESCRIPTOR = {
    'ALIAS_FILTER': [0., 0.],
    'AMPLITUDE_RECOVERY': None,
    'BAND_REJECT_FILTER': [0., 0., 0., 0.],
    'CDP_NUMBER': 0,
    'CDP_TRACE': 0,
    'CHANNEL_NUMBER': 0,
    'DATUM': 0.,
    'DELAY': 0.,
    'DESCALING_FACTOR': 0.,
    'DIGITAL_BAND_REJECT_FILTER': [0., 0., 0., 0.],
    'DIGITAL_HIGH_CUT_FILTER': [0., 0.],
    'DIGITAL_LOW_CUT_FILTER': [0., 0.],
    'END_OF_GROUP': 0,
    'FIXED_GAIN': None,
    'HIGH_CUT_FILTER': [0., 0.],
    'LINE_ID': None,
    'LOW_CUT_FILTER': [0., 0.],
    'NOTCH_FREQUENCY': 0.,
    'POLARITY': 1.,
    'RAW_RECORD': None,
    'RECEIVER': None,
    'RECEIVER_GEOMETRY': [0.],
    'RECEIVER_LOCATION': [0.],
    'RECEIVER_SPECS': [None, None],
    'RECEIVER_STATION_NUMBER': 1,
    'SAMPLE_INTERVAL': 1.,
    'SHOT_SEQUENCE_NUMBER': 1,
    'SKEW': 0.,
    'SOURCE': None,
    'SOURCE_GEOMETRY': [0.],
    'SOURCE_LOCATION': [0.],
    'SOURCE_STATION_NUMBER': 1,
    'STACK': 1,
    'STATIC_CORRECTIONS': [None, None, None],
    'TRACE_TYPE': 'UNKNOWN',
    'NOTE': '',
}

SUHEADER = {
    'tracl': np.int32, 'tracr': np.int32, 'fldr': np.int32,
    'tracf': np.int32, 'ep': np.int32, 'cdp': np.int32,
    'cdpt': np.int32, 'trid': np.int16, 'nvs': np.int16,
    'nhs': np.int16, 'duse': np.int16, 'offset': np.int32,
    'gelev': np.int32, 'selev': np.int32, 'sdepth': np.int32,
    'gdel': np.int32, 'sdel': np.int32, 'swdep': np.int32,
    'gwdep': np.int32, 'scalel': np.int16, 'scalco': np.int16,
    'sx': np.int32, 'sy': np.int32, 'gx': np.int32,
    'gy': np.int32, 'counit': np.int16, 'wevel': np.int16,
    'swevel': np.int16, 'sut': np.int16, 'gut': np.int16,
    'sstat': np.int16, 'gstat': np.int16, 'tstat': np.int16,
    'laga': np.int16, 'lagb': np.int16, 'delrt': np.int16,
    'muts': np.int16, 'mute': np.int16, 'ns': np.uint16,
    'dt': np.uint16, 'gain': np.int16, 'igc': np.int16,
    'igi': np.int16, 'corr': np.int16, 'sfs': np.int16,
    'sfe': np.int16, 'slen': np.int16, 'styp': np.int16,
    'stas': np.int16, 'stae': np.int16, 'tatyp': np.int16,
    'afilf': np.int16, 'afils': np.int16, 'nofilf': np.int16,
    'nofils': np.int16, 'lcf': np.int16, 'hcf': np.int16,
    'lcs': np.int16, 'hcs': np.int16, 'year': np.int16,
    'day': np.int16, 'hour': np.int16, 'minute': np.int16,
    'sec': np.int16, 'timebas': np.int16, 'trwf': np.int16,
    'grnors': np.int16, 'grnofr': np.int16, 'grnlof': np.int16,
    'gaps': np.int16, 'otrav': np.int16, 'd1': np.float32,
    'f1': np.float32, 'd2': np.float32, 'f2': np.float32,
    'ungpow': np.float32, 'unscale': np.float32, 'ntr': np.int32,
    'mark': np.int16, 'shortpad': np.int16,
    'unassignedInt1': np.int32, 'unassignedInt2': np.int32,
    'unassignedInt3': np.int32, 'unassignedInt4': np.int32,
    'unassignedFloat1': np.float32, 'unassignedFloat2': np.float32,
    'unassignedFloat3': np.float32,
}


def _read_file_descriptor(fpointer):
    """
    This function reads and stores informations from the
    `file descriptor block`.

    :param fpointer: pointer containing the file to read
    """

    # Read the first sub-block of the descriptor block (32 bytes)
    descriptor_subblock = fpointer.read(32)

    # Get the block identifier
    block_id = unpack(b'bb', descriptor_subblock[0:2])

    # Deduce endianess
    if(block_id[0] == 85 and block_id[1]==58):
        # Little-endian
        endian = b'<'
    if(block_id[0] == 58 and block_id[1]==85):
        # Big-endian
        endian = b'>'

    # Get the revision ID
    revision_id = unpack(endian+b'H', descriptor_subblock[2:4])[0]

    # Get the size of the trace pointer sub-block (M)
    trace_pointer_subblock_size = unpack(endian+b'H', descriptor_subblock[4:6])[0]

    # Get the number of traces in file (N)
    number_of_traces = unpack(endian+b'H', descriptor_subblock[6:8])[0]

    # Get string terminator size and character
    string_term_size = unpack(endian+b'B', descriptor_subblock[8:9])[0]
    string_term_char = unpack(endian+b'c', descriptor_subblock[9:10])[0]
    if string_term_size == 2:
        string_term_char += unpack(endian+b'c', descriptor_subblock[10:11])[0]

    # Get line terminator size and character
    line_term_size = unpack(endian+b'B', descriptor_subblock[11:12])[0]
    line_term_char = unpack(endian+b'c', descriptor_subblock[12:13])[0]
    if line_term_size == 2:
        line_term_char += unpack(endian+b'c', descriptor_subblock[13:14])[0]

    # ------------------------------------------------------------
    # Reserved sub-block
    # Bytes 14 through 31 are reserved.
    # ------------------------------------------------------------

    # Read the trace pointer sub-block (bytes 32 through 32+[4(N-1)])
    trace_pointer_subblock = fpointer.read(trace_pointer_subblock_size)

    # Get pointers to trace descriptor blocks
    trace_pointer = []
    for itrace in range(0, number_of_traces):
        index = itrace*4
        pointer = unpack(endian+b'L', trace_pointer_subblock[index:index+4])[0]
        trace_pointer.append(pointer)

    # Read the free format section
    free_form_pointer = fpointer.read(2) #608-32+64)
    free_form_offset = unpack(endian+b'h', free_form_pointer[0:2])[0]
    while(free_form_offset != 0):
        text_free_form= ''
        text_pointer = fpointer.read(free_form_offset-2)
        for i in range(0, free_form_offset-2):
            text_free_form += unpack(endian+b's', text_pointer[i:i+1])[0].decode()
        key = text_free_form.split()[0]
        if key in FILE_DESCRIPTOR:
            FILE_DESCRIPTOR[key] = ' '.join(text_free_form.split()[1:])
        free_form_pointer = fpointer.read(2) #608-32+64)
        free_form_offset = unpack(endian+b'h', free_form_pointer[0:2])[0]

    return endian, revision_id, trace_pointer, dict(FILE_DESCRIPTOR), string_term_char, line_term_char

def _read_traces(seg2stream, fpointer, endian, trace_pointer, string_term_char, line_term_char, scalco, scalel):
    """
    This function reads and stores informations from the
    `trace descrptior block` and `trace data block`.

    :param seg2stream: Stream object
    :param fpointer: pointer containing the file to read
    :param endian: endianess
    :param trace_pointer: pointer to the trace descriptor
    """

    # Get the number of traces
    ntraces = np.size(trace_pointer)

    # Loop over traces
    for itrace in range(0, ntraces):
        # Seek trace position in file
        fpointer.seek(trace_pointer[itrace], 0)
        # Read the trace descriptor
        trace_descriptor = fpointer.read(32)
        # Get the block size
        size_block = unpack(endian+b'H', trace_descriptor[2:4])[0]
        # Get the size of the corresponding data block
        size_data_block = unpack(endian+b'L', trace_descriptor[4:8])[0]
        # Get the number of samples
        ns = unpack(endian+b'L', trace_descriptor[8:12])[0]
        # Get the data code
        data_code = unpack(endian + b'B', trace_descriptor[12:13])[0]
        if data_code == 1:
            seg2stream.datatype = np.int16
        if data_code == 2:
            seg2stream.datatype = np.int32
        if data_code == 3:
            print('20-bit floating point is unsupported')
        if data_code == 4:
            seg2stream.datatype = np.float32
        if data_code == 5:
            seg2stream.datatype = np.float64
        # Read the free format section
        free_form_pointer = fpointer.read(2) #608-32+64)
        free_form_offset = unpack(endian+b'h', free_form_pointer[0:2])[0]

        # Create
        if itrace == 0:
            seg2stream.create(np.zeros((ntraces, ns), dtype=seg2stream.datatype))
            seg2stream.ntrac = ntraces

        seg2stream.trace_descriptor.append(dict(TRACE_DESCRIPTOR))

        while(free_form_offset != 0):

            # Declare a temporary header
            #tmp_header = dict(TRACE_DESCRIPTOR)

            text_free_form= ''
            text_pointer = fpointer.read(free_form_offset-2)

            for i in range(0, free_form_offset-2):
                text_free_form += unpack(endian+b's', text_pointer[i:i+1])[0].decode()
            key = text_free_form.split()[0]

            if key in TRACE_DESCRIPTOR:
                TRACE_DESCRIPTOR[key] = ' '.join(text_free_form.split()[1:])
                seg2stream.trace_descriptor[itrace][key] = ' '.join(text_free_form.split()[1:])

            if key == 'SAMPLE_INTERVAL':
                delta = np.float64(TRACE_DESCRIPTOR[key].rstrip(string_term_char.decode()).split())
                seg2stream.trace_descriptor[itrace][key] = delta[0]

            if key == 'DATUM':
                datum = np.float64(TRACE_DESCRIPTOR[key].rstrip(string_term_char.decode()))
                seg2stream.trace_descriptor[itrace][key] = datum

            if key == 'DELAY':
                delay = float(TRACE_DESCRIPTOR[key].rstrip(string_term_char.decode()))
                seg2stream.trace_descriptor[itrace][key] = delay

            if key == 'RECEIVER_LOCATION':
                srecloc = (TRACE_DESCRIPTOR[key].rstrip(string_term_char.decode())).split()
                recloc = []
                for i in range(len(srecloc)):
                    recloc.append(float(srecloc[i]))
                seg2stream.trace_descriptor[itrace][key] = recloc

            if key == 'SOURCE_LOCATION':
                ssrcloc = (TRACE_DESCRIPTOR[key].rstrip(string_term_char.decode())).split()
                srcloc = []
                for i in range(len(ssrcloc)):
                    srcloc.append(float(ssrcloc[i]))
                seg2stream.trace_descriptor[itrace][key] = srcloc
            free_form_pointer = fpointer.read(2) #608-32+64)
            free_form_offset = unpack(endian+b'h', free_form_pointer[0:2])[0]

        # Seek trace position in file
        fpointer.seek(trace_pointer[itrace], 0)
        fpointer.read(size_block)
        data_array = np.frombuffer(fpointer.read(ns*data_code), dtype=np.float32)

        seg2stream.traces[itrace, :] = data_array[:]

        # -------------------------------------
        # Convert SEG2 to SU/CWP rev0 format
        # -------------------------------------

        # Trace number in line
        hdrtype = SUHEADER['tracl']
        seg2stream.header[itrace]['tracl'] = hdrtype(itrace+1)

        # Trace number in reel
        hdrtype = SUHEADER['tracr']
        seg2stream.header[itrace]['tracr'] = hdrtype(itrace+1)

        # Trace number in file
        hdrtype = SUHEADER['tracf']
        seg2stream.header[itrace]['tracf'] = hdrtype(itrace+1)

        # Trace identification code
        hdrtype = SUHEADER['trid']
        if seg2stream.trace_descriptor[itrace]['TRACE_TYPE'] == 'UNKNOW': #tmp_header['TRACE_TYPE'] == 'UNKNOWN':
            seg2stream.header[itrace]['trid'] = hdrtype(0)
        if seg2stream.trace_descriptor[itrace]['TRACE_TYPE'] == 'SEISMIC_DATA': #tmp_header['TRACE_TYPE'] == 'SEISMIC_DATA':
            seg2stream.header[itrace]['trid'] = hdrtype(1)
        if seg2stream.trace_descriptor[itrace]['TRACE_TYPE'] == 'DEAD': #tmp_header['TRACE_TYPE'] == 'DEAD':
            seg2stream.header[itrace]['trid'] = hdrtype(2)
        if seg2stream.trace_descriptor[itrace]['TRACE_TYPE'] == 'TEST_DATA': #tmp_header['TRACE_TYPE'] == 'TEST_DATA':
            seg2stream.header[itrace]['trid'] = hdrtype(3)
        if seg2stream.trace_descriptor[itrace]['TRACE_TYPE'] == 'UPHOLE': #tmp_header['TRACE_TYPE'] == 'UPHOLE':
            seg2stream.header[itrace]['trid'] = hdrtype(4)

        # Number of samples
        hdrtype = SUHEADER['ns']
        seg2stream.header[itrace]['ns'] = hdrtype(ns)

        # Sample interval
        if delta < 1.e-6:
            hdrtype = SUHEADER['dt']
            seg2stream.header[itrace]['dt'] = hdrtype(np.float32(delta)*np.float32(1000.)*np.float32(1000000.))
            seg2stream.units0 = 'milliseconds'
        else:
            hdrtype = SUHEADER['dt']
            seg2stream.header[itrace]['dt'] = hdrtype(delta*1000000.)

        # Delay
        if delay  < 1:
            delay *= 1000.
            hdrtype = SUHEADER['delrt']
            seg2stream.header[itrace]['delrt'] = hdrtype(delay)

        # Coordinates
        #calc_scalco = False
        #scalco = 1
        #while(calc_scalco == False):
        #    tmpscale = []
        #    for i in range(len(recloc)):
        #        test = (recloc[i]*scalco).is_integer()
        #        tmpscale.append(test)
        #    for i in range(len(srcloc)):
        #        test = (srcloc[i]*scalco).is_integer()
        #        tmpscale.append(test)

        #    # Check validity (all value must be integer)
        #    if(False in tmpscale and scalco < 10000.):
        #        scalco *= 10
        #    else:
        #        calc_scalco = True
        #        if scalco >= 10000:
        #            scalco = 10000.


        hdrtype = SUHEADER['scalco']
        if(scalco < 1):
            seg2stream.header[itrace]['scalco'] = hdrtype(scalco)
            # Fill coordinates
            if len(recloc) == 1:
                hdrtype = SUHEADER['gx']
                seg2stream.header[itrace]['gx'] = hdrtype(recloc[0]*abs(scalco))
            else:
                hdrtype = SUHEADER['gx']
                seg2stream.header[itrace]['gx'] = hdrtype(recloc[0]*abs(scalco))
                seg2stream.header[itrace]['gy'] = hdrtype(recloc[1]*abs(scalco))
            if len(srcloc) == 1:
                hdrtype = SUHEADER['sx']
                seg2stream.header[itrace]['sx'] = hdrtype(srcloc[0]*abs(scalco))
            else:
                hdrtype = SUHEADER['sx']
                seg2stream.header[itrace]['sx'] = hdrtype(srcloc[0]*abs(scalco))
                seg2stream.header[itrace]['sy'] = hdrtype(srcloc[1]*abs(scalco))

        if(scalco >= 1):
            seg2stream.header[itrace]['scalco'] = hdrtype(scalco)
            # Fill coordinates
            if len(recloc) == 1:
                hdrtype = SUHEADER['gx']
                seg2stream.header[itrace]['gx'] = hdrtype(recloc[0]/scalco)
            else:
                hdrtype = SUHEADER['gx']
                seg2stream.header[itrace]['gx'] = hdrtype(recloc[0]/scalco)
                seg2stream.header[itrace]['gy'] = hdrtype(recloc[1]/scalco)
            if len(srcloc) == 1:
                hdrtype = SUHEADER['sx']
                seg2stream.header[itrace]['sx'] = hdrtype(srcloc[0]/scalco)
            else:
                hdrtype = SUHEADER['sx']
                seg2stream.header[itrace]['sx'] = hdrtype(srcloc[0]/scalco)
                seg2stream.header[itrace]['sy'] = hdrtype(srcloc[1]/scalco)

        # Elevation
        # Coordinates
        #calc_scalel = False
        #scalel = 1
        #if(len(recloc) != 3 and len(srcloc) != 3):
        #    calc_scalel = True
        #while(calc_scalel == False):
        #    tmpscale = []
        #    if len(recloc) == 3:
        #        test = (recloc[2]*scalel).is_integer()
        #        tmpscale.append(test)
        #    if len(srcloc) == 3:
        #        test = (srcloc[2]*scalel).is_integer()
        #        tmpscale.append(test)
        #    if seg2stream.trace_descriptor[itrace]['DATUM'] != 0: #tmp_header['DATUM'] != 0.:
        #        test = (datum*scalel).is_integer()
        #        tmpscale.append(test)
        #    # Check validity (all value must be integer)
        #    if(False in tmpscale and scalel < 10000.):
        #        scalel *= 10
        #    else:
        #        calc_scalel = True
        #        if scalel >= 10000.:
        #            scalel = 10000.

        hdrtype = SUHEADER['scalel']
        seg2stream.header[itrace]['scalel'] = hdrtype(-1*scalel)
        if len(recloc) == 3:
            hdrtype = SUHEADER['gelev']
            seg2stream.header[itrace]['gelev'] = hdrtype(recloc[2]*scalel)
        if len(srcloc) == 3:
            hdrtype = SUHEADER['selev']
            seg2stream.header[itrace]['selev'] = hdrtype(srcloc[2]*scalel)
        if seg2stream.trace_descriptor[itrace]['DATUM'] != 0.: #tmp_header['DATUM'] != 0.:
            hdrtype = SUHEADER['gdel']
            seg2stream.header[itrace]['gdel'] = hdrtype(datum*scalel)
            seg2stream.header[itrace]['sdel'] = hdrtype(datum*scalel)

        # counit type 6 is specific to IFSTTAR REDUCED-SCALE MODELING
        if seg2stream.file_descriptor['UNITS'] == 'FEET' or seg2stream.file_descriptor['UNITS'] == 'METERS':
            seg2stream.header[itrace]['counit'] = 1
            if seg2stream.file_descriptor['UNITS'] == 'FEET':
                seg2stream.units1 = 'feet'
            if seg2stream.file_descriptor['UNITS'] == 'METERS':
                seg2stream.units1 = 'meters'
        if seg2stream.file_descriptor['UNITS'] == 'INCHES' or seg2stream.file_descriptor['UNITS'] == 'CENTIMETERS':
            seg2stream.header[itrace]['counit'] = 5
            if seg2stream.file_descriptor['UNITS'] == 'INCHES':
                seg2stream.units1 = 'inches'
            if seg2stream.file_descriptor['UNITS'] == 'CENTIMETERS':
                seg2stream.units1 = 'centimeters'
        if seg2stream.file_descriptor['UNITS'] == 'MILLIMETERS':
            seg2stream.header[itrace]['counit'] = 6
            seg2stream.units1 = 'millimeters'


def seg2scan(fname):
    """
    Scan the SEG-2 file and return the file header and trace headers.
    """

    scalco = 1
    scalel = 1

    try:
        # Try to open file
        fpointer = open(fname, 'rb')
        # Create a Stream object
        seg2stream = Stream()
        # File format
        seg2stream.format = 'seg-2'
        # Read the file header
        endian, seg2stream.revision, trace_pointer, seg2stream.file_descriptor, string_term_char, line_term_char = _read_file_descriptor(fpointer)
        # Read trace descriptor and data blocks
        _read_traces(seg2stream, fpointer, endian, trace_pointer, string_term_char, line_term_char, scalco, scalel)

        return seg2stream.file_descriptor, seg2stream.trace_descriptor

    except FileNotFoundError:
        pass

def seg2read(fname, **options):
    """
    Read SEG-2 files and store in NESSI data structure.

    :param fname: SEG-2 filename and path

    .. rubric:: Basic usage

    >>> # Import seg2read from nessi package
    >>> from nessi.io import seg2read
    >>> # Read SEG-2 file
    >>> sdata = seg2read('NESSI_TEST_DATA.seg2')

    """

    # Get options
    scalco = options.get('scalco', 1)
    scalel = options.get('scalel', 1)

    try:
        # Try to open file
        fpointer = open(fname, 'rb')
        # Create a Stream object
        seg2stream = Stream()
        # File format
        seg2stream.format = 'seg-2'
        # Read the file header
        endian, seg2stream.revision, trace_pointer, seg2stream.file_descriptor, string_term_char, line_term_char = _read_file_descriptor(fpointer)
        # Read trace descriptor and data blocks
        _read_traces(seg2stream, fpointer, endian, trace_pointer, string_term_char, line_term_char, scalco, scalel)

        return seg2stream

    except FileNotFoundError:
        pass
