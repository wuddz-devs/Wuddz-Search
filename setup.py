from setuptools import setup, find_packages
import os


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as wr:
	readme=wr.read()

setup(
    name='wuddz_search',
    version='1.0.0',
	description='*ALL IN 1, File/Folder Searcher, Parser & Archiver (Encryption Optional)',
	long_description=readme,
	long_description_content_type="text/markdown",
	author='Wuddz_Devs',
	author_email='wuddz_devs@protonmail.com',
    packages=find_packages(include=['wuddz_search', 'wuddz_search.*']),
    entry_points={'console_scripts': ['wudz-spa=wuddz_search.search:cli_main']},
    license='MIT',
	classifiers=[
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3.10',
    ],
)
