# -*- coding: utf-8 -*-

from fabric.api import cd
from fabric.api import env
from fabric.api import run


env.user = 'ubuntu'
env.hosts = ['ec2-34-241-206-136.eu-west-1.compute.amazonaws.com']
env.forward_agent = True


def update():
    u"""Function defining all steps required to properly update application."""
    with cd('/home/ubuntu/gittraining/'):
        run('git pull')
    
    run('sudo nginx -s reload')