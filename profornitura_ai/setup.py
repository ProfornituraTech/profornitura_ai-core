from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="profornitura_ai",
    version="0.0.1",
    description="Profornitura AI - Tender Automation Platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Profornitura Italia SRL",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
)
