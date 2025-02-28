#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy.
"""

from fabric.api import *
from os import path

env.user = 'ubuntu'
env.hosts = ['35.174.208.54', '34.229.72.105']

def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if not path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        file_name = archive_path.split("/")[-1]
        file_no_ext = file_name.split(".")[0]
        remote_path = "/data/web_static/releases/{}/".format(file_no_ext)
        run("sudo mkdir -p {}".format(remote_path))
        run("sudo tar -xzf /tmp/{} -C {}".format(file_name, remote_path))
        run("sudo rm /tmp/{}".format(file_name))

        # Move contents, remove unnecessary directory, and create symlink
        run("sudo mv -f {}web_static/* {}".format(remote_path, remote_path))
        run("sudo rm -rf {}web_static".format(remote_path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(remote_path))
        print("New version deployed!")
        return True
    except Exception as e:
        print(e)
        return False
