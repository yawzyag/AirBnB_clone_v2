#!/usr/bin/python3
"""coment for my file"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """making a file"""
    local("sudo mkdir -p versions")
    name_archive = "versions/web_static_{}.tgz".format(
        datetime.now().strftime("%Y%m%d%H%M%S"))
    local("sudo tar -zvcf {} web_static".format(name_archive))
    return name_archive
