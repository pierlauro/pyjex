from setuptools import setup, find_packages
from codecs import open
from os import path

setup(
	name = 'pyjex',

	version = '1.0.0',

	description = 'Java formatting for Python exceptions',

	author = 'pierlauro',

	author_email = 'sciarellip+pyjex@gmail.com',

	url = 'https://github.com/pierlauro/pyjex',

	classifiers = [
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
	],

	keywords = 'exceptions stacktrace formatting',

	packages = find_packages( exclude = ['tests'] ),

	license = 'Public Domain',

	project_urls = {
		'Bug Tracker': 'https://github.com/pierlauro/pyjex/issues',
		'Source': 'https://github.com/pierlauro/pyjex',
	}
)
