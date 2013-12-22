from setuptools import setup, find_packages

setup(
    name='genaa',
    version='0.0',
    packages=find_packages(),
    url='https://github.com/hirokiky/genaa',
    license='MIT',
    author='hirokiky',
    author_email='hirokiky@gmail.com',
    description='',
    entry_points={
        'console_scripts': [
            'genaa = genaa.commands.main:run',
        ],
    },
)
