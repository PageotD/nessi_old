*********************************
SEG2 format
*********************************


The SEG2 format was described by Pullan (1990) and supported as a technical
standard by the Society of Exploration Geophysics (SEG). It is one of the most
widely used seismic (/radar) data format.

FORMAT_DESCRIPTION

File descriptor
=================================

The file descriptor is a mixed binary/textual header containing general informations
about the data.

When reading a SEG2 file with NeSSI, the textual header is stored in an object
variable called ``file_descriptor``.   
