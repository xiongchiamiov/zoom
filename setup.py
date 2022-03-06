#!/usr/bin/env python3

from setuptools import setup

setup(
    name='zoom_shortener',
    version='0.2.0',
    url='https://github.com/xiongchiamiov/zoom',
    author='James Pearson Hughes',
    author_email='pearson@changedmy.name',
    install_requires=(
        'Flask >= 2.0.0, < 3.0.0',
        'gevent >= 21.12.0',
    ),
    packages=['zoom_shortener'],
    package_data={
        'zoom_shortener': ['templates/*', 'schema.sql'],
    },
    scripts=['bin/zoom'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
