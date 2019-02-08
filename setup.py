from setuptools import setup

setup(
    name='slackbot',
    version='1.0',
    description='Car Lookup - Slackbot',
    author='Alexander Bij',
    author_email='AlexanderBij@GoDataDriven.com',
    packages=['slackbot'],
    install_requires=['Flask>=1.0.2',
                      'tornado>=4.5',
                      'slackclient>=1.3.0',
                      'requests',
                      'pandas',
                      'tenacity']
)