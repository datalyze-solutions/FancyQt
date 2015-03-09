
from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

import fancyqt

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

tests_require = ['pytest']
setup(
    name='FancyQt',
    version=fancyqt.__version__,
    url='https://github.com/datalyze-solutions/FancyQt',
    license='MIT License',
    namespace_packages = ['fancyqt'],
    author='Matthias Ludwig - Datalyze Solutions',
    tests_require=tests_require,
    install_requires=[],
    cmdclass={'test': PyTest},
    author_email='m.Ludwig@datalyze-solutions.com',
    description='Provides modern stylesheets for Qt 4.x.',
    long_description=long_description,
    packages=['fancyqt'],
    include_package_data=True,
    platforms='any',
    test_suite='tests',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: German',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: User Interfaces'
        ],
    extras_require={
        'testing': tests_require,
    }
)