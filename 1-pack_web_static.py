#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """do_pack method"""

    date = datetime.now()
    date_str = date.strftime('%Y%m%d%H%M%S')
    local('mkdir -p versions')
    path = 'versions/web_static_' + date_str + '.tgz'
    tar = 'tar -cvzf {} web_static'.format(path)

    if local(tar):
        return None
    return path

if __name__ == '__main__':
    do_pack()
