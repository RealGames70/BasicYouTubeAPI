from io import open
from setuptools import setup

"""
:authors: Real72
"""

version = '0.0.1'

setup(
	name='club_house_api',
	version=version,

	author='Real72',
	author_email='peoplesdreamer@gmail.ru',


	url='https://github.com/Peopl3s/club_house_api',
	download_url=''

	license='Apache License, Version 2.0, see LICENSE file',

	packages=['basic-yt-api'],
	install_requires=['loguru', 'google-api-python-client'],

	classifiers=[
		'Operating System :: OS Independent',
		'Intended Audience :: End Users/Desktop',
		'Intended Audience :: Developers',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: Implementation :: PyPy',
		'Programming Language :: Python :: Implementation :: CPython',
	]
)