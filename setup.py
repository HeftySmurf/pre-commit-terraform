from setuptools import find_packages
from setuptools import setup


setup(
    name='pre-commit-terraform',
    description='Pre-commit hooks for terraform_docs',
    url='https://github.com/HeftySmurf/pre-commit-terraform',
    version_format='{tag}+{gitsha}',

    author='Contributors',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages(exclude=('tests*', 'testing*')),
    install_requires=[
        'setuptools-git-version',
    ],
    entry_points={
        'console_scripts': [
            'tf_docs = terraform_docs.tf_docs:main',
        ],
    },
)