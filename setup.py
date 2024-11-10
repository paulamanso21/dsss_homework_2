from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    tests_require=[],
    test_suite="tests",
    author="Paula Manso Zorrilla",
    author_email="paulamanso21@gmail.com",
    description="Math quiz game application",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/paulamanso21/dsss_homework_2.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
