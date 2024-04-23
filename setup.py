#!/usr/bin/env python

from setuptools import setup

with open("test_requirements.txt") as f:
    test_requirements = f.readlines()

setup(
    name="dtgogtd",
    version="0.0.1",
    description="DAT to GPX or GPX to DAT",
    author="Dzmitry Padabed",
    author_email="itfarrier@icloud.com",
    url="https://github.com/itfarrier/dtgogtd",
    packages=["dtgogtd"],
    test_suite="test.test_suite",
    tests_require=test_requirements,
)
