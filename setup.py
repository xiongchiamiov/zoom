#!/usr/bin/env python3

from setuptools import setup

setup(
    name='zoom_shortener',
    version='0.2.0',
    url='https://github.com/xiongchiamiov/zoom',
    author='James Pearson Hughes',
    author_email='pearson@changedmy.name',
    install_requires=(
        'Flask >= 0.11.1, < 0.12',
        'gevent >= 1.2.0, < 2.0',
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
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
