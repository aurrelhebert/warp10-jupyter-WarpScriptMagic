try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import io
from os import path

here = path.abspath(path.dirname(__file__))

install_requires = [
    'ipython>=1.0',
]

setup(
    name='warpscriptmagic',
    version='0.1.1',
    description='Magics to use Warp10 in IPython notebook.',
    long_description="long_description",

    # Author details
    author='ahebert',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Programming Language :: Python :: 3.4',
    ],

    # What does your project relate to?
    keywords='warp10 ipython notebook javascript',

    py_modules=['warpscriptmagic'],
    install_requires=install_requires,
)