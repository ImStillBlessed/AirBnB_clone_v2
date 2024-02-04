#!/usr/bin/python3
"""
Compress web static package
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
        print(f"Error: Archive '{archive_path}' not found.")
        return False

    try:
        # Extract file name and file name without extension
        file_name = path.basename(archive_path)
        file_no_ext = path.splitext(file_name)[0]

        # Remote path for deployment
        remote_path = "/data/web_static/releases/{}/".format(file_no_ext)

        # Upload archive
        put(archive_path, "/tmp/")

        # Create directory and extract archive
        run("sudo mkdir -p {}".format(remote_path))
        run("sudo tar -xzf /tmp/{} -C {}".format(file_name, remote_path))

        # Remove archive from /tmp
        run("sudo rm /tmp/{}".format(file_name))

        # Use rsync to move contents, remove unnecessary directory, and create symlink
        run("sudo rsync -av --ignore-existing {}/web_static/ {}/".format(remote_path, remote_path))
        run("sudo rm -rf {}web_static".format(remote_path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(remote_path))

        print("New version deployed!")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
        
