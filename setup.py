from setuptools import setup
import os

# Read version from __init__.py
with open(os.path.join('cli2web', '__init__.py'), 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.split('=')[1].strip().strip("'").strip('"')
            break

setup(
    version=version
) 