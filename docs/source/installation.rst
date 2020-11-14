*********************************
Installation
*********************************

Requirements
=================================

NeSSI has the following minimum requirements:

* `Python <https://www.python.org/>`_ 3.5+
* `Numpy <http://www.numpy.org/>`_
* `Scipy <http://www.scipy.org/>`_
* `Matplotlib <http://www.matplotlib.org/>`_

Installing NeSSI
=================================

Using pip
---------------------------------

Actually, *PyPi* reveals some issues for packages build with `linux_x86_64`
plateforms. It seems quite complicated to create an installable source package.


Using conda
---------------------------------

NeSSI can be installed via the conda package manager using `Anaconda Distribution <https://www.anaconda.com/distribution/>`_ (recommanded) or `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_ .
The main advantage is that all package dependencies are taken care of at the time of download and NeSSI will be ready for use as soon as it is installed. Be sure to create a virtual environment with Python 3.5, 3.6 or 3.7.

Once you have created a virtual environment with conda, you can install NeSSI very easily.

With Anaconda-navigator, add the ``pageotd`` channel and search for the ``nessi`` package and install it.
Or, on the command line, in your virtual environment:

.. code-block:: console

   conda install -c pageotd nessi


Building from source
=================================

Additionnal requirements
---------------------------------

Building from source requires:

* a compiler suite (*i.e.* `GCC <https://gcc.gnu.org>`_)
* `Python-dev <https://www.python.org/>`_ package
* `Setuptools <https://setuptools.readthedocs.io/en/latest/>`_ package
* `Cython <https://cython.org>`_

Obtaining the source package from git repository
------------------------------------------------

The lastest development version of NeSSI can be cloned from framagit:

.. code-block:: console

   git clone https://framagit.org/PageotD/nessi.git

Building and installing
---------------------------------

It is recommended to use a conda virtual environment. The nessi folder contains an ``environment.yml`` file to create an environment suitable for compiling and using NeSSI:

.. code-block:: console

   conda env create -f environment.yml


To build and install NeSSI, go to the root of the source folder and run:

.. code-block:: console

   python setup.py install

Be sure that the `python` command points to Python version 3.5 or later using the command:

.. code-block:: console

   python -V
