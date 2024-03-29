import pathlib

import pkg_resources
from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


with open(path.join(here, "VERSION")) as file:
    version = file.read().strip()


with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setup(

    name='podrostoc',

    version=version,

    description='Convert different document in tree structure',

    long_description=long_description,

    long_description_content_type='text/markdown',


    url='https://github.com/IlyaKozlov/podrostoc',

    author='ISP RAS',

    author_email='ilya-kozlov2@yandex.ru',

    install_requires=install_requires,

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],

    python_requires='>=3.6, <4',

)
