#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='manheim_hello_world_app',
    version='0.1.0',
    description="A simple hello world app for use with AWS Elastic Beanstalk",
    long_description=readme + '\n\n' + history,
    author="Marcellus Easley",
    author_email='marcellus.easley@gmail.com',
    url='https://github.com/marcelluseasley/manheim_hello_world_app',
    packages=[
        'manheim_hello_world_app',
    ],
    package_dir={'manheim_hello_world_app':
                 'manheim_hello_world_app'},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='manheim_hello_world_app',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
