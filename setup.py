try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config={
        'description': 'Web-scraper built in python3',
        'author': 'Omar Shariff @kabeershariff',
        'url': 'URL to get',
        'download_url': 'where to download it',
        'author_email': 'kabeershariff@protonmail.com',
        'version': '0.1',
        'install_requires': [],
        'packages': [],
        'scripts': [],
        'name': 'web-scraper-python3'
        }

setup(**config)
