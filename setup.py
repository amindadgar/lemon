from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="lemon-explainer-research-use",
    version="1.0.0",
    author="Dennis Collaris",
    maintainer="Mohammad Amin Dadgar",
    maintainer_email="dadgaramin96@gmail.com",
    packages=find_packages(),
    description="lemon-explainer package updated for research usages.",
    long_description=open("README.md").read(),
    install_requires=requirements,
    long_description_content_type='text/markdown',
)