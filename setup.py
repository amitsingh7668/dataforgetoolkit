from setuptools import setup, find_packages

setup(
    name='dataforgetoolkit',
    version='1.0.3',
    setup_requires=['wheel'],
    packages=find_packages(),
    url='https://github.com/amitsingh7668/dataforgetoolkit',
    license='Amit Singh',
    author='Amit Singh',
    author_email='2singh.amit3@gmail.com',
    description='It is a library that facilitates converting CSV files to various formats (such as DataFrames or other CSV/Excel files) based on a JSON mapping',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
