from setuptools import setup, find_packages

setup(
    name="django_request_logger",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    license="MIT License",
    description="A Django app to log requests.",
    # long_description=open("README.md").read(),
    # long_description_content_type="text/markdown",
    url="https://github.com/yourusername/django_request_logger",
    author="Your Name",
    author_email="your.email@example.com",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: X.Y",  # Replace "X.Y" as appropriate
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    install_requires=[
        "Django>=2.2",
    ],
)
