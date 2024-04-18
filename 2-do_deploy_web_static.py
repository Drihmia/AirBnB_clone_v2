#!/usr/bin/python3
""" This module contains the do_deploy function using Fabric module"""
from fabric.api import run, put, env, cd
from os import path

env.hosts = ["34.207.120.158", "54.237.107.28"]
# , "54.237.107.28"
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"


def do_deploy(archive_path):
    """a Fabric script (based on the file 1-pack_web_static.py) that
    distributes an archive to your web servers, using the function
    do_deploy"""

    if not path.exists(archive_path) or not ("web" in archive_path):
        return False
    if not ("tgz" in archive_path):
        return False

    # file name would be like this, as example:
    # file name:  web_static_20240317155811.tgz
    file_name = path.basename(archive_path)

    # target name and file name with no exstention, it would be sth like:
    # path target: /data/web_static/releases/web_static_20240317155811
    file_name_no_ext = file_name.split(".")[0]
    path_target = f"/data/web_static/releases/{file_name_no_ext}"

    # upload the file name to servers, it would be sth like:
    # tmp dest:  /tmp/web_static_20240317155811.tgz
    tmp_file = f"/tmp/{file_name}"

    # upload the tgz file from local to servers.
    put(archive_path, "/tmp")

    # creating the path if it does not exist.
    run_mkdir_cmd = f"sudo mkdir -p {path_target}"
    run(run_mkdir_cmd)
    run("sudo chown -R ubuntu:ubuntu /data/")

    # remove old resources: files and directories, before extrating and moving
    # with cd(path_target):
    # run("rm -rf *")

    # Uncompress the archive to the folder
    # /data/web_static/releases/web_static_20240317155811
    # on the web server
    run_tar_cmd = f"tar -xzf {tmp_file} -C {path_target}"
    run(run_tar_cmd)

    # remove the temporary file from /tmp directory in the server(s)
    run(f"sudo rm {tmp_file}")

    # mv the content from target/web_static to target/
    run(f"cp -rf {path_target}/web_static/* {path_target}/")

    # remove the old directory
    run(f"sudo rm -rf {path_target}/web_static")

    # remove the symbolic link
    smblc_link = "/data/web_static/current"
    run("sudo rm -rf {}".format(smblc_link))

    # recreate symblic link
    run(f"ln -sf {path_target}/ {smblc_link}")

    return True
