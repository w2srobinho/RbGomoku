import os
from distutils.core import setup

from setuptools import find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'rbgomoku',
    version = '1.1',
    license = 'MIT',
    description = 'The abstract strategy board game',
    author = 'Willian de Souza (Robinho)',
    author_email = 'willianstosouza@gmail.com',
    packages = find_packages('rbgomoku'),
    package_dir = {'rbgomoku': 'src'},
    install_requires = ['numpy==1.11.0'],
    test_suite = 'nose.collector',
    tests_require = ['nose==1.3.7'],
    long_description=read('README.md')
)
