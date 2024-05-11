from setuptools import setup, find_packages

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Education",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

setup(
    name="rest_api_response",
    version="0.1.1",
    description="A go-to production API response with an easy format for building APIs with Python.", # noqa: E501
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
    url="https://github.com/aybruhm/api-response",
    author="Abraham 'Abram' Israel",
    author_email="israelvictory87@gmail.com",
    license="MIT",
    classifiers=classifiers,
    keywords=["api", "response", "custom api response"],
    packages=find_packages(),
)
