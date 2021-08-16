import setuptools

with open("ComputMath/README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ComputMath",

    version="1.0.0",

    author="Popckov Sergio",

    author_email="popckovM10@yandex.ru",

    description="Computational Mathematics Package",

    long_description=long_description,

    long_description_content_type="text/markdown",

    url="https://github.com/PopckovS/Computational_Mathematics",

    packages=setuptools.find_packages(),

    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux 18.04",
    ],

    python_requires='>=3.6',
)