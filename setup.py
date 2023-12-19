from setuptools import setup, find_packages

setup(
    name='cpq_tools',
    version='0.1',
    author='Daniel Helkey',
    author_email='dhelkey@stanford.edu',
    description='Package containg Python functoins for data analysis intended for CPQCC/CMQCC usage, developed by Daniel Helkey',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dhelkey/cpq_tools',
    packages=find_packages(),
    install_requires=[
        'pandas', 
        'numpy', 
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
