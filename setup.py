from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="kalalang",
    version="0.1.0",
    author="Yahia Kala",
    author_email="yahiakalabs@gmail.com",
    description="Convenience functions for working with language models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yahiakala/kalalang",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)