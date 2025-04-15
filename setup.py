from setuptools import setup, find_packages

setup(
    name="any-agents",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["any-agent"],
    description="Redirect package for any-agent - you probably meant to install 'any-agent' instead",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/any-agent",
    author="Your Name",
    author_email="your.email@example.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ],
)