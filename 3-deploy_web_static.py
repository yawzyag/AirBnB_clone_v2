#!/usr/bin/python3
"""coment for my file"""
from fabric.api import local, sudo, run, put, env
from datetime import datetime
from os.path import exists
env.hosts = ["35.231.255.39", "35.196.178.86"]


def do_pack():
    """making a file"""
    local("sudo mkdir -p versions")
    name_archive = "versions/web_static_{}.tgz".format(
        datetime.now().strftime("%Y%m%d%H%M%S"))
    local("sudo tar -zvcf {} web_static".format(name_archive))
    return name_archive


def do_deploy(archive_path):
    """deploying"""
    if exists(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        file_arc = archive_path.split("/")[1].split(".")[0]
        path = "/data/web_static/releases/{}".format(file_arc)
        print(path)
        run("mkdir {}".format(path))
        run("tar -xvzf /tmp/{}.tgz -C {}/".format(file_arc, path))
        run("sudo rm /tmp/{}".format(archive_path.split("/")[1]))
        run("sudo rm /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/{}\
        /data/web_static/current".
            format(file_arc))
        run("sudo mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}".
            format(file_arc, file_arc))
        run("rm -rf /data/web_static/releases/{}/web_static/".format(file_arc))
        return True
    except BaseException:
        return False


def deploy():
    """holisdh this is a comment"""
    junito_var = do_pack()
    if junito_var:
        return do_deploy(junito_var)
    else:
        return False
