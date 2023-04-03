from setuptools import setup, find_packages
from pathlib import Path


def get_version():
    try:
        from setuptools_scm import get_version
        return get_version(local_scheme="no-local-version")
    except ImportError:
        print("setuptools_scm not installed, using default version '0.0'")
        return "0.0"

with open(Path(__file__).parent.parent / 'README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
  name="umep-reqs",
  version=get_version(), # Use setuptools_scm to get version from git tags.
  packages=find_packages(),
  install_requires=[
      "supy==2022.9.22", # Replace with actual dependency and version number.
    #   "dependency2==y.y.y" # Replace with actual dependency and version number.
  ],
  author="UMEP dev team",
  long_description=long_description,
  long_description_content_type='text/markdown',
)