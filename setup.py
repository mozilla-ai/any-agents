from setuptools import setup, find_packages

setup(
    name="any-agents",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["any-agent"],
    description="Redirect package for any-agent - you probably meant to install 'any-agent' instead",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mozilla-ai/any-agents",
    author="Nathan Brake",
    author_email="nathan@mozilla.ai",
)
