import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

setup(
    name='genaa',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/hirokiky/genaa',
    license='MIT',
    author='hirokiky',
    author_email='hirokiky@gmail.com',
    description='genaa, a ASCII Art generator.',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.3",
            "Development Status :: 3 - Alpha",
            "Topic :: Processing :: Filters",
            "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        'console_scripts': [
            'genaa = genaa.commands.main:run',
        ],
    },
)
