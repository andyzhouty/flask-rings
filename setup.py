"""
    flask-rings
    ~~~~~~~~~~~~~
    Rings helper for flask.
    :copyright: (c) 2021 by Andy Zhou
    :license: LGPL-3.0, see License for more details.
"""
from os import path
from codecs import open
from setuptools import setup


basedir = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(basedir, 'README.md'), encoding="utf-8") as file_obj:
    long_description = file_obj.read()

setup(
    name="Flask-Rings",
    version="0.4.2",
    url="https://github.com/ringsings/flask-rings",
    license="LGPL-3.0",
    author="Andy Zhou",
    author_email="zhoutianyou11@gmail.com",
    description="Rings(https://github.com/ringsings/Rings) helper for flask.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    platforms="any",
    packages=["flask_rings"],
    zip_safe=False,
    test_suite="tests",
    include_package_data=True,
    install_requires=[
        "Flask",
        "Flask-WTF"
    ],
    keywords="flask extension development rings",
    classifiers={
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    }
)
