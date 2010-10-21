# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

# Utility function to read the README file.  
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(name='redsolutioncms.django-chunks',
      version=__import__('chunks').__version__,
      description=read('DESCRIPTION'),

      author='Clint Ecker',
      author_email='me@clintecker.com',

      url='http://code.google.com/p/django-chunks/',

      packages=find_packages(),

      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],

      include_package_data=True,
      zip_safe=False,
      long_description=read('README'),

      entry_points={
        'redsolutioncms': ['chunks = chunks.redsolution_setup', ],
        }
      )
