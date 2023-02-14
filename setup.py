from setuptools import setup, find_packages

setup(
    name = "mypackage",
    version = "0.1",
    packages = find_packages(exclude =["tests"] ),
    liscense = 'MIT',
    long_description = open('README.md').read(),
    install_requires = ["numpy"],
    url = 'https://github.com/<username>/<package-name',
    author = "<Lishivha N>",
    author_email = '<your Email>'
)
