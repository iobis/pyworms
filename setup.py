from setuptools import setup

setup(
    name="pyworms",
    description="Python client for the WoRMS REST service",
    author="Pieter Provoost",
    author_email="pieterprovoost@gmail.com",
    version="0.4.0",
    packages=["pyworms"],
    install_requires=["backports.functools_lru_cache", "requests"],
    license="BSD",
)
