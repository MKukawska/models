import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="object_detection",
    version="1.10.0",
    author="Tensorflow Object Detection API",
    author_email="",
    description="A package wraping Tensorflow Object Detection API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tensorflow/models/tree/master/research/object_detection",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)