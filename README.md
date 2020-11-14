![Powered by PYTHON](https://www.python.org/static/community_logos/python-powered-w-100x40.png)
![LGPL3 logo](https://www.gnu.org/graphics/lgplv3-88x31.png)

[![coverage report](https://framagit.org/PageotD/nessi/badges/master/coverage.svg)](https://framagit.org/PageotD/nessi/commits/master)

NeSSI (Near-Surface Seismic Imaging) aims to provide python modules for the rapid development of seismic inversion codes based on global optimization method.

## Getting started

### Prerequisites

__NeSSI__ requires __Python 3.5+__, __cython__, __numpy__, __scipy__ and __matplotlib__. You also need __git__ installed on your computer.

To get a copy of __NeSSI__ :

```bash
$ git clone https://framagit.com/PageotD/nessi.git
```

In the nessi folder, check for update:

```bash
$ git pull
```

### Installation

Install dependencies with ```pip```:

```bash
pip install -r requirements.txt
```

An alternative is to install the `conda` package manager via the installation of Anaconda software or Miniconda and create a new environment using the `environment.yml` file:

```bash
conda env create -f environment.yml
```

Finally, go to the downloaded folder and run

```bash
python setup.py develop
```

## Contribute

[How to contribute](CONTRIBUTE.md)

## License

NeSSI is an open-source project licensed under the [LGPLv3](http://www.gnu.org/licenses/lgpl-3.0-standalone.html).
