girder_jupyterhub
=================

girder_jupyterhub is a python package that implements a JupyterHub authenticator, that
allows a user to authenticate using a Girder token.

Configuration
=============

Add the following options to your :code:`jupyterhub_config.py`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    c.JupyterHub.authenticator_class = 'girder_jupyterhub.auth.GirderAuthenticator'


This extension uses `authentication state <https://jupyterhub.readthedocs.io/en/stable/reference/authenticators.html/>`_
to store Girder-Tokens. In production this requires the following environment variable to be set.

    export JUPYTERHUB_CRYPT_KEY=<key>

Where <key> is the result of running:

    openssl rand -hex 32


