# -*- coding: utf-8 -*-
# @Time    : 1/10/21
# @Author  : Daniel Ordoñez
# @email   : daniels.ordonez@gmail.com

from distutils.core import setup
from setuptools import find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="slip-control",
    version="0.0.1",
    description="Spring Loaded Inverted Pendulum control and visualization python tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Daniel Ordonez",
    author_email="daniel.ordonez@gmail.com",
    url="https://github.com/Danfoa/slip_control",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["numpy", "scipy", "matplotlib", "tqdm", "cvxpy"],
    python_requires=">=3.6",
)
