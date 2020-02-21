import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pylog-koverstreet",
    version="0.0.1",
    author="Kyle Overstreet",
    author_email="koverstreet@gmail.com",
    description="A package for creating data logs and sending emails.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kyle1/pylog",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)