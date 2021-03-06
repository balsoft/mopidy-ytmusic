# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ''

setup(
    long_description=readme,
    name='Mopidy-YTMusic',
    version='0.2.2',
    description='Mopidy extension for playling music/managing playlists in Youtube Music',
    python_requires='==3.*,>=3.7.0',
    author='Ozymandias (Tomas Ravinskas)',
    author_email='tomas.rav@gmail.com',
    license='Apache-2.0',
    entry_points={"mopidy.ext": ["ytmusic = mopidy_ytmusic:Extension"]},
    packages=['mopidy_ytmusic'],
    package_dir={"": "."},
    package_data={"mopidy_ytmusic": ["*.conf"]},
    install_requires=[
        'mopidy==3.*,>=3.0.2', 'youtube-dl==2021.*,>=2021.1.1',
        'ytmusicapi==0.*,>=0.14.0'
    ],
    extras_require={
        "dev": [
            "dephell==0.*,>=0.8.0", "flake8==3.*,>=3.8.4",
            "setuptools==51.*,>=51.0.0", "sphinx==3.*,>=3.3.1"
        ]
    },
)
