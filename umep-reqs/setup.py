from setuptools import setup, find_packages


def get_version():
    try:
        from setuptools_scm import get_version
        return get_version()
    except ImportError:
        print("setuptools_scm not installed, using default version '0.0'")
        return "0.0"

setup(
  name="umep-reqs",
  version=get_version(), # Use setuptools_scm to get version from git tags.
  packages=find_packages(),
  install_requires=[
      "supy==2022.9.22", # Replace with actual dependency and version number.
    #   "dependency2==y.y.y" # Replace with actual dependency and version number.
  ],
  author="UMEP dev team",
)