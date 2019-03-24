# This is a script that tells pip how to setup your
# code on the system. You don't need to make any
# changes to it, nor do you need to call it yourself.
# pip runs it for you when you type commands.

from setuptools import setup

setup(
    name='distancepi',
    version='1.0.0-devel',
    description='Client for RaspberryPi to get and display messages',
    long_description='',
    url='https://github.com/MattBussing/DistancePi',
    author='Matt Bussing',
    author_email='mbussing@mines.edu',
    license='',

    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],

    packages=['distancepi'],
    python_requires='>=3.5, <4',
    install_requires=[
        'pytest>=3.8'],

    entry_points={
        'console_scripts': [
            'distancepi=distancepi.__main__:main',
        ],
    },
)
