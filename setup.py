#!/usr/bin/env python3
from setuptools import setup
from distutils.core import setup, Extension
import os
from get_include_paths import *

module = Extension('setup_test', 
                    sources = [
                        'sub/setup_pybind11.cpp'
                        ],
                    include_dirs=[
                        get_pybind_include(user=True),
                        get_eigen_include(user=True),
                        get_boost_include(user=True),
                        ],
                    extra_compile_args=['-std=c++11', '-fpermissive'],
                    )
 
setup (name = 'setup_test',
        version = '1.0',
        description = 'Intersections is a library to find the aric of two data sets.',
        setup_requires=[
            'wget >= 3.1',
            'pybind11'
        ],
        ext_modules = [module])