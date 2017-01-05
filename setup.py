#!/usr/bin/env python3

from setuptools import setup

setup(
    name='zoom_shortener',
    version='0.1.1',
    url='https://github.com/xiongchiamiov/zoom',
    author='James Pearson Hughes',
    author_email='pearson@changedmy.name',
    install_requires=(
        'Flask >= 0.11.1, < 0.12',
        'gevent >= 1.2.0, < 2.0',
    ),
    packages=['zoom_shortener'],
    package_data={
        'zoom_shortener': ['templates/*'],
    },
    scripts=['bin/zoom'],
)
