from setuptools import setup, find_packages

setup(
    name='subbruter',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'dnspython',
        'colorama'
    ],
    entry_points={
        'console_scripts': [
            'subbruter = subbruter.main:cli'
        ]
    },
    author='Mubtasim Fuad',
    description='Advanced Subdomain Bruteforcing Tool with HTTP/DNS Support',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/SubBruter',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=3.6',
)

