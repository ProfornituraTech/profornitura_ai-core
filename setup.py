from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

setup(
    name="profornitura_ai",
    version="0.1.0",
    description="Profornitura AI – ERPNext + AI Automation per gare d'appalto (Gare, ANAC, TimelineAI, AutoDecisionAI, DocAI, Logging, Cleanup).",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Profornitura Italia SRL",
    author_email="vittorio.erp.ai@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    license="MIT",
)
