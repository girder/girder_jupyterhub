# single-user docker images for use with JupyterHub and DockerSpawner
# Enables Girder content manager and updates jupyterlab 
FROM jupyterhub/singleuser
MAINTAINER Chris Harris <chris.harris@kitware.com>

RUN conda update -y jupyterlab

RUN  pip install git+https://github.com/cjh1/girder_jupyter.git@master

RUN echo "c.NotebookApp.contents_manager_class = 'girder_jupyter.contents.girderfilemanager.GirderFileManager'" >> ~/.jupyter/jupyter_notebook_config.py
