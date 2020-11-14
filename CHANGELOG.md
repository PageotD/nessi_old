# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [0.3.1] - 2019-11-12

## Fixed
- *graph* method for *Stream* class now handles correctly one-trace data
- *wind* method for *Stream* class now sets the correct value for the `delrt` keyword

## [0.3.0] - 2019-10-10

### Added
- *.gitlab* folder for *issue templates*
- *.gitlab-ci.yml* file for gitlab CI/CD
- *requirements.txt* for ``pip``
- *MANIFEST.in* for source distribution packaging
- *seg2read* in *io* module for seg2 format support
- *mute* method in *Stream* class
- *getfilter* in *nessi.signal.filtering*
- *seg2scan* in *seg2format* to scan SEG-2 file before SU-CWP conversion
- *nessi.graphics.graph* equivalent of `suxgraph`
- *graph* method added to *Stream* class
- *dispick* method for *Stream* object to pick (semi-auto) the effective dispersion curve

### Modified
- *setup.py* with cythonize
- update *README.md*
- update *CONTRIBUTE.md*
- update *environment.yml* for sharing conda environment
- *Stream* now supports 16-bit fixed point, 32-bit fixed point, 32-bit floating
  point and 64-bit floating point data
- *file_descriptor* and *trace_descriptor* attributes in Stream object to store
  file headers from read files (*i.e.* seg-2)
- *gethdr* method now supports trace selection using parameters (*imin* and *count*)
- *susrcinv* is now in cython (for performance)
- *sin2filter* in *nessi.signal.filtering*
- *avg* in *nessi.signal.operations*
- *_check_format* in *nessi.io.suformat*
- clean *seg2format* in *nessi.io*
- *Stream* to handle module modifications (signal, ...)
- *seg2read* does not search automatically best values for `scalco` and `scalel`; these values can be now passed as arguments

### Fixed
- correcting 'label' in *image* and *wiggle* methods
- *dispick* method for dispersion diagram effective curve extraction
- *write* method for ``dt<1.e-6`` (``issue #9``)
- *gethdr* method (``issue #11``)
- *operation* method for *Stream* object

### Removed
- useless *Makefile*

## [X.X.X] - YYYY-MM-DD
### Added
### Fixed
### Removed
