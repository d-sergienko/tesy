#!/usr/bin/env python3

from setuptools import setup

setup(
    name='tesy',
    version='0.1.0',
    description='Python for Tesy water heaters',
    author='Dmitry Sergienko',
    author_email='dmitry.sergienko@gmail.com',
    license='BSD',
    keywords='tesy',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3 :: Only'
    ],
    url='https://github.com/d-sergienko/tesy',
    packages=['tesy'],
    install_requires=[
        'requests',
        'setuptools',
    ]
)