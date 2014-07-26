#!/bin/env python
# -*- coding: utf-8 -*-

'''Django package for fancybox:
Tool that offers a nice and elegant way to add zooming functionality
for images, html content and multi-media on your webpages.
'''

from setuptools import setup

setup(
    name='django-fancybox',
    version='2.1.5',
    url='https://fancyapps.com',
    description=globals()['__doc__'],
    author='Janis Skarnelis',
    maintainer='Renat Galimov',
    maintainer_email='renat2017@gmail.com',
    license='CC BY-NC 3.0',
    keywords=['django', 'fancybox'],
    platforms='any',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=['django_fancybox'],
)
