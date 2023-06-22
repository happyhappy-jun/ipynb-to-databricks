import warnings
from os import environ, path

from setuptools import find_packages, setup

setup_args = dict(
    name="ipynb_to_databricks",
    version=version,
    author="Byungjun Yoon",
    author_email="bjyoon513@gmail.com",
    description="Convert ipynb to databricks style python file",
    packages=find_packages(exclude=["tests"]),
    entry_points={"console_scripts": ["jupytext = jupytext.cli:jupytext"]},
    tests_require=["pytest"],
    install_requires=[],
    python_requires="~=3.6",
    extras_require={},
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Framework :: Jupyter",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Text Processing :: Markup",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)