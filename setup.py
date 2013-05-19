#! /usr/bin/env python
# coding:utf-8

from setuptools import setup
import os


def read_file(filename):
    filepath = os.path.join(
        os.path.dirname(__file__),
        filename)
    return open(filepath).read()

setup(
    name="fusha",
    version="0.1",
    description="Easily customizable progress bar module",
    author="Noriyuki Abe",
    author_email="kenko.py@gmail.com",
    url="https://github.com/kenkov/fusha",
    py_modules=["fusha"],
    long_description=read_file("README.rst"),
    license="MIT License",
)
