from setuptools import setup, find_packages
import os

# Read version from __init__.py
with open(os.path.join('cli2web', '__init__.py'), 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.split('=')[1].strip().strip("'").strip('"')
            break

setup(
    version=version,
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'cli2web': [
            'templates/*.html',
            'templates/*',
            'static/*',
            'static/**/*',
        ],
    },
    zip_safe=False,
) 