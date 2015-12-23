# -*- coding: utf-8 -*-
from setuptools import setup

__author__ = 'viruzzz-kun'
__version__ = '0.1'


if __name__ == '__main__':
    setup(
        name="pysimplelogs2",
        version=__version__,
        description="Simplelogs client library",
        long_description='',
        author='Bars Group',
        author_email="viruzzz.soft@gmail.com",
        license='BSD',
        url="http://stash.bars-open.ru/scm/medvtr/pysimplelogs2",
        include_package_data=True,
        packages=['pysimplelogs2'],
        platforms='any',
        zip_safe=False,
        install_requires=[
            'requests',
        ],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ])
