#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
from os import path
from setuptools import setup


read = lambda filepath: codecs.open(filepath, 'r', 'utf-8').read()


README_PATH = path.abspath(path.join(path.dirname(__file__), 'readme.txt'))

setup(
    name = "liquor",
    version = "0.1",
    author = "Nahim Nasser",
    author_email = "nnasser@gmail.com",
    url = 'http://git.io/NM2urA',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    description = 'A simple Django app to download LCBO Product Data.',
    packages=[
        'liquor',
        'liquor.management',
        'liquor.management.commands',
    ],
    long_description= read(README_PATH),
    install_requires=[
        'Django>=1.4',
        "requests>=1.1.0",
        "simplejson>=3.1.2",
    ],
)