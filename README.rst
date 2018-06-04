girder_jupyterhub
=================

girder_jupyterhub is a python package that implements a JupyterHub authenticator, that
allows a user to authenticate using a Girder token.

Configuration
=============

Add the following options to your :code:`jupyterhub_config.py`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    c.JupyterHub.authenticator_class = 'girder_jupyterhub.auth.GirderAuthenticator'





