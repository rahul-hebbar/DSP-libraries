import setuptools

def readme():
    with open("README.md", "r") as fh:
        long_description = fh.read()
    return long_description

setuptools.setup(
    name="aud_fea", # Replace with your own username
    version="0.1.0",
    author="Rahul_Hebbar",
    author_email="rhin1998@gmail.com",
    description="Extract audio features",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/rahul-hebbar/DSP-libraries/tree/master/feature-extraction",
    license="MIT",
    packages = setuptools.find_packages(),
    install_requires=["numpy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)