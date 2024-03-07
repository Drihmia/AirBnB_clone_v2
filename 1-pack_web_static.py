#!/usr/bin/env python3
""" This module contains the do_pack function using Fabric module"""
from fabric.api import local
from os import path, mkdir
from datetime import datetime


def do_pack():
    """a Fabric script that generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone repo, using the
    function do_pack."""
    try:
        if not path.exists("versions/"):
            mkdir("versions/")

        current_datetime = datetime.now()
        time = current_datetime.strftime("%Y%m%d%H%M%S")

        # archiving the files in web_static directory
        archive_path = "versions/web_static_{}.tgz".format(time)

        # announecement for packing
        packing = "Packing web_static to {}".format(archive_path)
        print(packing)

        # executing the tar command
        cmd_archive = "tar -cvzf {} web_static".format(archive_path)
        local(cmd_archive)

        size = path.getsize(archive_path)
        # announecement for being packed
        packed = "web_static packed: {} -> {}Bytes".format(archive_path, size)
        print(packed)

        return archive_path
    except Exception as f:
        return None
