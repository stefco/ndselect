#!/usr/bin/env python

from setuptools import setup

setup(
    setup_requires=[
        'setuptools_scm',
    ],
    use_scm_version={
        'write_to': 'ndselect/version.py',
    },

    name = 'ndselect',
    description='NDS2-based GUI LIGO channel browser/ndscope launcher',
    author='Stefan Trklja Countryman',
    author_email='stefan.countryman@gmail.com',
    url='https://git.ligo.org/stefco/ndselect',
    license='GNU GPL v3+',

    packages=['ndselect'],

    install_requires=[
        'PyQt5',
        'nds2-client',
        'gpstime',
        'ndscope',
    ],

    package_data={
        'ndscope': [
            '*.ui',
            'data/default_channel_tree/*/*/*/*.json',
        ],
    },

    # https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/
    entry_points={
        'console_scripts': [
            'ndselect = ndselect.__main__:main',
            ],
        }
)
