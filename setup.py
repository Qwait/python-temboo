from setuptools import find_packages
from setuptools import setup

version = '1.76'

setup(**dict(
    version=version,
    name='temboo',
    description='Python wrapper for the python Temboo SDK',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python'
    ],
    packages=find_packages()
))
