from distutils.core import setup

from flask_voluptuous import __version__

setup(
  name = 'flask_voluptuous',
  py_modules = ['flask_voluptuous'], # this must be the same as the name above
  version = __version__,
  description = 'A simple flask extension for data validation with Voluptuous',
  author = 'Ludovico O. Russo',
  author_email = 'ludus.russo@gmail.com',
  url = 'https://github.com/ludusrusso/flask_voluptuous/tree/develop', # use the URL to the github repo
  download_url = 'https://github.com/ludusrusso/flask_voluptuous/tree/develop/archive/{0}.tar.gz'.format(__version__), # I'll explain this in a second
  keywords = ['voluptous', 'flask', 'validation'], # arbitrary keywords
  classifiers = [],
  install_requires=[
        'Flask', 'Voluptuous'
    ],
)
