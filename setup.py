from distutils.core import setup
import setuptools


setup(
    name='ninageweb',
    version='',
    install_requires=[
        'flask',
        'flask_assets',
        'jsmin'
    ],
    packages=[
        'ninageweb'
    ],
    entry_points={
        "console_scripts": [
        ]
    }
)
