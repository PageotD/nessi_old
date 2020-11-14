.. NeSSI documentation master file, created by
   sphinx-quickstart on Wed Mar 13 10:07:50 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

NeSSI (Near-Surface Seismic Imaging) is a set of python modules for near-surface seismic applications. It contains, among other things, modules for signal processing and data inversion using global optimization methods such as the particle swarm method.

NeSSI is an open-source project licensed under the LGPLv3.

Getting started
=================================

.. toctree::
    :maxdepth: 1

    installation
    contribute

User documentation
=================================

Supported data format
---------------------------------


Actually, NeSSI supports two type of seismic (/radar) data format:

.. toctree::
    :maxdepth: 1

    io_su_format
    io_seg2_format

Modeling
---------------------------------

.. toctree::
    :maxdepth: 1

    fdpsv_methods

Signal processing
---------------------------------

.. toctree::
   :maxdepth: 1

   class_stream

Global optimization
---------------------------------

.. toctree::
    :maxdepth: 1

    class_swarm
    class_genalg


Examples
---------------------------------

.. toctree::
    :maxdepth: 1

    read_write_and_create_SU_data
    

Developer documentation
=================================


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
