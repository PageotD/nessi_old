# Contributing to NeSSI

This document aims to give an overview of how to contribute to NeSSI.

## Getting started

To contribute, you must have:
* a __FramaGit__ account ([framagit register](https://framagit.org/users/sign_in?redirect_to_referer=yes))
* __git__ installed on your system ([download and install](https://git-scm.com/downloads))
* a development version of __NeSSI__ (only for developers)

More informations on how to use __git__ are available on the [git official documentation](https://git-scm.com/doc) and the [GitHub cheat sheet](https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf).

## Submitting an Issue

Before submitting an issue, please search through [existing issues](https://framagit.org/PageotD/nessi/issues) to avoid duplicates.

If you want to post a problem or a bug, please check that you have provided essential informations:

* __problem/bug description:__ A clear and concise description of what the bug is.
* __to reproduce:__ A small piece of code which reproduces the issue (with as few as possible external dependencies).
* __NeSSI version__, __python version__, __numpy version__, ...
* __platform__ OS+version (Debian 9, Ubuntu 16.10, ...)
* __virtual environement__ yes/no; if yes, which one.

## Submitting a Pull Request

Before submitting a pull request:
* be sure that the feature/hotfix that you want to add does not already exist.

1. Fork the repository.
2. Make a new branch. For feature additions/changes or bugfixes, base your new branch at `master`.        
  * Feature branches must be named `features/name_of_the branch`.
  * Bugfix branches must be named `bugfixes/name_of_the_issue`.
3. Add a test for your change. Only refactoring and documentation changes require no new tests.
4. Make the test pass.
5. Push to your fork and submit a pull request. Set the base branch to `master`
6. Wait for our review. We may suggest some changes or improvements or alternatives.

All the submitted pieces including potential data must be compatible with the LGPLv3 license and will be LGPLv3 licensed as soon as they are part of NeSSI. Sending a pull request implies that you agree with this.

Additionally take care to not add big files. Even for tests we generally only accept files that are very small.

## Developer installation

The first step is to clone your fork of the __NeSSI__ repository using `git clone` command.

The easy way to install the development version of __NeSSI__ is to first install the `conda` package manager on your system via [Anaconda](https://www.anaconda.com/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html). Then, use `conda` to install the development environment:

```bash
conda env create -f environment.yml
```

Activate the virtual environement:

```bash
conda activate nessi-dev
```

Then, run the setup script:

```bash
cd /directory/where/code/lives
# Run the setup script
python setup.py develop
# Create a new branch
git checkout -b features/name_of_the_branch
```
