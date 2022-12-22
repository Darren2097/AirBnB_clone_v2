#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy"""

from fabric.api import local, env, run, put, sudo


env.hosts = ['54.160.122.13', '54.145.241.141']


def do_deploy(archive_path):
    """do_deploy method"""

    if archive_path:
        archive_file = archive_path.split('/')[1]
        archive_dir = archive_file.split('.')[0]
        releases = '/data/web_static/releases/'
        current = '/data/web_static/current'

        try:
            put(archive_path, '/tmp/')
            run('mkdir -p {}{}'.format(releases, archive_dir))
            run('tar -xzf /tmp/{} -C {}{}'.format(
                archive_file, releases, archive_dir))
            run('rm /tmp/{}'.format(archive_file))
            run('mv {}{}/web_static/* {}{}'.format(
                releases, archive_dir, releases, archive_dir))
            run('rm -rf {}{}/web_static'.format(releases, archive_dir))
            run('rm -rf {}'.format(current))
            run('ln -s {}{} {}'.format(releases, archive_dir, current))

            return True
        except:
            return False
    else:
        return False
