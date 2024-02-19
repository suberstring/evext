from setuptools import setup, find_packages

setup(
    name="evext",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],

    author="suberstring",
    author_email="enjoyrainy@126.com",
    description="Awa",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/suberstring/evext",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
)