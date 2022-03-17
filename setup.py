#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DeepLabCut2.0-2.2 Toolbox (deeplabcut.org)
© A. & M. Mathis Labs
https://github.com/DeepLabCut/DeepLabCut
Please see AUTHORS for contributors.
https://github.com/DeepLabCut/DeepLabCut/blob/master/AUTHORS
Licensed under GNU Lesser General Public License v3.0
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deeplabcut",
    version="2.2.0.6",
    author="A. & M. Mathis Labs",
    author_email="alexander@deeplabcut.org",
    description="Markerless pose-estimation of user-defined features with deep learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DeepLabCut/DeepLabCut",
    install_requires=[
        "dataclasses",
        "ipython",
        "filterpy",
        "ruamel.yaml>=0.15.0",
        "imgaug>=0.4.0",
        "numba",
        "matplotlib",
        "networkx",
        "numpy",
        "pandas",
        "scikits.image>=0.17,<=0.18.1",
        "scikit-learn",
        "scipy>=1.4",
        "statsmodels",
        "pytables<=3.6.1",
        "tensorflow>=2.0",
        "tqdm~=4.43.0",
        "pyyaml",
        "Pillow>=7.1",
    ],
    scripts=["deeplabcut/pose_estimation_tensorflow/models/pretrained/download.sh"],
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ),
    entry_points="""[console_scripts]
            dlc=dlc:main""",
)

# https://www.python.org/dev/peps/pep-0440/#compatible-release
