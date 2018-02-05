# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
  name = 'markdown-jinja',
  version = '0.1.0',
  py_modules = ['markdown_jinja'],
  description = 'Python Markdown extension which adds Jinja2 support',
  author = 'Józef Sokołowski',
  author_email = 'pypi@qzb.me',
  url = 'https://github.com/qzb/markdown-jinja/',
  download_url = 'https://github.com/qzb/markdown-jinja/archive/v0.1.0.tar.gz',
  classifiers = [
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Intended Audience :: Developers',
    'Topic :: Communications :: Email :: Filters',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
    'Topic :: Internet :: WWW/HTTP :: Site Management',
    'Topic :: Software Development :: Documentation',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Text Processing :: Filters',
    'Topic :: Text Processing :: Markup :: HTML'
  ],
  install_requires = ['Markdown>=2.6', 'Jinja2>=2.10']
)
