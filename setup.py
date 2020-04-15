from os.path import join, dirname
from setuptools import setup, find_packages

import image_comparsion


setup(
    name='PyImageComparsion',
    version=image_comparsion.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    include_package_data=True,
    install_requires=[line.rstrip() for line in open("requirements.txt", "r").readlines()],
    test_suite='tests'
)