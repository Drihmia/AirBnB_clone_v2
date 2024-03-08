#!/usr/bin/python3
""" this module contains do_clean function based on Fabric module"""
from fabric.api import run, local, lcd, cd, env

env.hosts = ["100.26.168.177", "54.237.107.28"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"


def do_clean(number=0):
    """a Fabric script (based on the file 3-deploy_web_static.py) that
    deletes out-of-date archives, using the function do_clean
    """
    try:
        number = int(number)
    except Exception as f:
        return

    if number == 0 or number == 1:
        with lcd("versions"):
            try:
                number_files = int(local("ls -1t | grep web | wc -l",
                                         capture=True))
            except (ValueError, TypeError) as e:
                number_files = 0
            if number_files >= 2:
                number_files = number_files - 1
                local(f"rm $(ls -1t | grep web | tail -{number_files})")

        with cd("/data/web_static/releases"):
            try:
                number_files = int(run("ls -1t | grep web | wc -l"))
                print("-------", number_files)
            except (ValueError, TypeError) as e:
                number_files = 0
            if number_files >= 2:
                number_files = number_files - 1
                run(f"rm -rf $(ls -1t | grep web | tail -{number_files})")
    else:
        with lcd("versions"):
            try:
                number_files = int(local("ls -1t | grep web | wc -l",
                                         capture=True))
            except (ValueError, TypeError) as e:
                number_files = 0
            if number_files > number:
                number_files = number_files - number
                local(f"rm $(ls -1t | grep web | tail -{number_files})")

        with cd("/data/web_static/releases"):
            try:
                number_files = int(run("ls -1t | grep web | wc -l"))
                print("-------", number_files)
            except (ValueError, TypeError) as e:
                number_files = 0
            if number_files >= number:
                number_files = number_files - number
                run(f"rm -rf $(ls -1t | grep web | tail -{number_files})")
