#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 09:21:40 2020

@author: alberttenigin
"""


setup(
    name="Python opencv numpy face detection",
    version="alfa",
    description="Face and eyes detection",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/teniginalbert/computer_vision",
    author="Albert Tenigin",
    author_email="teniginalbert@gmail.com",
    license="MOPTEX Ltd",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=[""],
    include_package_data=True,
    install_requires=[
        "opencv", "numpy", "sys", "os"
    ],
)