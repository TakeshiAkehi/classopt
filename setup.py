import ast
import re
import os

from setuptools import setup , find_packages

PACKAGE_NAME = 'classopt'
PACKAGE_SUBS = []

# with open(os.path.join(PACKAGE_NAME, '__init__.py')) as f:
#     match = re.search(r'__version__\s+=\s+(.*)', f.read())
# version = str(ast.literal_eval(match.group(1)))
version = "0.0.1"

setup(
    # metadata
    name=PACKAGE_NAME,
    version=version,

    # options
    packages=[PACKAGE_NAME],
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.8',
    install_requires=[],
    extras_require={
        'dev': [
            'pytest>=3',
        ],
    },
    entry_points='''
        [console_scripts]
        {app}={pkg}.cli:main
    '''.format(app=PACKAGE_NAME.replace('_', '-'), pkg=PACKAGE_NAME),
)