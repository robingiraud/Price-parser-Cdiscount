import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cdiscount_robin_clementine",
    version="0.0.1",
    author="Robin Giraud",
    author_email="robin.giraud5@gmail.com",
    description="Simple package to parse any Cdiscount product prices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/robingiraud/python-eval-robingiraud",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
