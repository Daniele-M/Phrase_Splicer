try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Daniele Massanti',
    'url': 'URL to get it at.',
    'dowload_url': 'Where to dowload it.',
    'author_email': 'da.massanti@gmail.com',
    'version': '0.1',
    'install_requirements': ['nose'],
    'packages': ['NAME'],
    'scrips': [],
    'name': 'projectname'
}

setup(**config)
