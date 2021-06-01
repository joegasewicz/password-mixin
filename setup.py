from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="password-mixin",
    version="0.1.2",
    description="Mixin that adds useful password methods to your Python objects",
    packages=["password_mixin"],
    py_modules=["password_mixin"],
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joegasewicz/password-mixin",
    author="Joe Gasewicz",
    author_email="joegasewicz@gmail.com",
)