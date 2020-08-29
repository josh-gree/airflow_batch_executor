# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['src']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'src',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'josh-gree',
    'author_email': 'joshua.greenhalgh@heyjobs.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
