#!/usr/bin/python3
""" This module contains the deploy function using Fabric module"""
from fabric.api import env

do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

env.hosts = ["100.26.168.177", "54.237.107.28"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"


def deploy():
    """a Fabric script (based on the file 2-do_deploy_web_static.py) that
    creates and distributes an archive to your web servers, using the function
    deploy"""

    # pack
    archive_path = do_pack()
    # return false if no archive has been created
    if not archive_path:
        return False

    # deploy
    value_do_deploy = do_deploy(archive_path)

    return value_do_deploy
