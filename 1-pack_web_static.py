#!/usr/bin/python3
"""
This is  a Fabric script that generates a .tgz archive
from the contents of the web_static folder of your AirBnB Clone repo,
using the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    stores all the files in web_static folder in tbz archive
    """
    now = datetime.now()
    now = now.strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static/' + now + '.tgz'

    local('mkdir -p versions/web_static')
    result = local('tar -cvzf {} web_static/'.format(archive_path))

    if result.return_code == 0:
        return archive_path
    return None
