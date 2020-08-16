import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "Fantasy-Basketball-Squad-Optimizer",
    version = "0.0.1",
    author = "Santi Tobon & Mack Cooper",
    description = "This program will help a user build the most optimal fantasy basketball team",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/santitobon9/Fantasy-Basketball-Squad-Optimizer",
    packages = setuptools.find_packages(),
    python_requires = ">=3.8.2"
)