#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import setuptools  # necessary even when numpy.distutils.core.setup is used

# Include extensions only when not on readthedocs.org
if os.environ.get('READTHEDOCS', None) == 'True':
    from setuptools import setup
    from distutils.core import Extension
    extensions = []
else:
    from numpy.distutils.core import setup, Extension

    extensions = [
        Extension(name='apexpy.fortranapex',
                  sources=['src/fortranapex/magfld.f', 'src/fortranapex/apex.f',
                           'src/fortranapex/makeapexsh.f90',
                           'src/fortranapex/apexsh.f90',
                           'src/fortranapex/checkapexsh.f90'])]

setup(ext_modules=extensions)
