from setuptools import setup, find_packages

setup(
    name="midnight",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    author="Your Name",
    author_email="your.email@example.com",
    description="A standard Python project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
