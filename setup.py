from setuptools import setup, find_packages
from htmlentities import __version__

README = open('README.rst').read()

setup(name='htmlentities',
      version=__version__,
      description='HTML Entities for Python',
      long_description=README,
      author='CobraTeam',
      author_email='andrewsmedina@gmail.com',
      packages=find_packages(),
      include_package_data=True,
      )
