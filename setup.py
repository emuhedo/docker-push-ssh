import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="docker-push-ssh",
    version="0.1.0",
    author="Bryan Thornbury",
    author_email="bryan@coherenceapi.com",
    description="Push local docker images to your remote servers via ssh without the hassle.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/coherenceapi/docker-push-ssh",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
    ],
    scripts=[
        "bin/docker-push-ssh"
    ]
)