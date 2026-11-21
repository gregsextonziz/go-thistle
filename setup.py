from setuptools import setup, find_packages

setup(
    name="go-thistle",
    version="3.3.4",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.1.0",
        "numpy>=1.26.0",
        "matplotlib>=3.8.0",
    ],
)
