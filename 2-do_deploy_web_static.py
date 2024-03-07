#!/usr/bin/python3
""" This module contains the do_deploy function using Fabric module"""
from fabric.api import run, put, env
from os import path


env.hosts = ["100.26.168.177", "54.237.107.28"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """a Fabric script (based on the file 1-pack_web_static.py) that
    distributes an archive to your web servers, using the function
    do_deploy"""

    try:
        if not path.exists(archive_path):
            return False

        # isolating the file name
        file_name = path.basename(archive_path)

        # target name and file name with no exstention
        file_name_no_ext = file_name.split(".")[0]
        path_target = f"/data/web_static/releases/{file_name_no_ext}/"

        # upload the file name to servers
        tmp_dest = f"/tmp/{file_name}"
        put(archive_path, tmp_dest)

        # creating the path if it does not exist
        if not path.exists(""):
            run_mkdir_cmd = f"mkdir -p {path_target}"
            run(run_mkdir_cmd)

        # mouve
        # Uncompress the archive to the folder
        # /data/web_static/releases/ <archive filename without extension>
        # on the web server
        run_tar_cmd = f"tar -xzf /tmp/{file_name} -C {path_target}"
        run(run_tar_cmd)

        # remove the temporary file from /tmp/ directory in the server(s)
        run(f"rm {tmp_dest}")

        # mv the content from target/web_static to target/
        run(f"mv -n {path_target}web_static/* {path_target}")

        # remove the old directory
        run(f"rm -rf {path_target}web_static/")
        # remove the symbolic link
        smblc_link = "/data/web_static/current/"
        run("rm -rf {}".format(smblc_link))

        # recreate symblic link
        run(f"ln -sf {path_target} {smblc_link}")

        # reload nginx so the new changes will take effect
        # run("sudo nginx -s reload")
        print("New version deployed!")

        return True
    except Exception as f:
        return False
