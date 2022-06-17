from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='slackbot',
    version='1.1',
    description='Car Lookup - Slackbot',
    author='Alexander Bij',
    author_email='AlexanderBij@GoDataDriven.com',
    packages=['slackbot'],
    install_requires=required,
    extras_require={
        'dev': [
            'pytest',
            'pytest-cov',
            'pytest-pep8',
            'pylint'
        ]
    }
)