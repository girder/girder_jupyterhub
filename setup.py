from setuptools import setup
from codecs import open
import os
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


def prerelease_local_scheme(version):
    """Return local scheme version unless building on master in CircleCI.
    This function returns the local scheme version number
    (e.g. 0.0.0.dev<N>+g<HASH>) unless building on CircleCI for a
    pre-release in which case it ignores the hash and produces a
    PEP440 compliant pre-release version number (e.g. 0.0.0.dev<N>).
    """

    from setuptools_scm.version import get_local_node_and_date

    if 'CIRCLE_BRANCH' in os.environ and \
       os.environ.get('CIRCLE_BRANCH') == 'master':
        return ''
    else:
        return get_local_node_and_date(version)


setup(
    name='girder-jupyterhub',
    use_scm_version={'local_scheme': prerelease_local_scheme},
    setup_requires=['setuptools_scm'],
    description='A JupyterHub authenticator for Girder tokens',
    long_description=long_description,

    url='https://github.com/cjh1/girder_jupyterhub',

    author='Kitware Inc',
    author_email='kitware@kitware.com',

    license='BSD 3-Clause',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='jupyter girder authentication data management',

    packages=['girder_jupyterhub', 'girder_jupyterhub.auth'],

    install_requires=[
        'jupyterhub>0.8',
        'traitlets',
        'tornado'
    ],

    extras_require={

    }
)
