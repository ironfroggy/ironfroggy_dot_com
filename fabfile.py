#!/usr/bin/env python
from fabric.api import *
import fabric.contrib.project as project
import datetime
import re
import os
import shutil
import sys
import SocketServer

from pelican.server import ComplexHTTPRequestHandler

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'calvin@ash-alpha.ironfroggy.com:22'
dest_path = '/var/www/www.ironfroggy.com/'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'

# Github Pages configuration
env.github_pages_branch = "gh-pages"

# Port for `serve`
PORT = 8000

def clean():
    """Remove generated files"""
    if os.path.isdir(DEPLOY_PATH):
        shutil.rmtree(DEPLOY_PATH)
        os.makedirs(DEPLOY_PATH)

def build():
    """Build local version of site"""
    local('pelican -s pelicanconf.py')

def rebuild():
    """`clean` then `build`"""
    clean()
    build()

def regenerate():
    """Automatically regenerate site upon file modification"""
    local('pelican -r -s pelicanconf.py')

def serve():
    """Serve site at http://localhost:8000/"""
    os.chdir(env.deploy_path)

    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def reserve():
    """`build`, then `serve`"""
    build()
    serve()

def preview():
    """Build production version of site"""
    local('pelican -s publishconf.py')

def cf_upload():
    """Publish to Rackspace Cloud Files"""
    rebuild()
    with lcd(DEPLOY_PATH):
        local('swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
              '-U {cloudfiles_username} '
              '-K {cloudfiles_api_key} '
              'upload -c {cloudfiles_container} .'.format(**env))

@hosts(production)
def publish():
    """Publish to production via rsync"""
    # local('pelican -s publishconf.py')
    # project.rsync_project(
    #     remote_dir=dest_path,
    #     exclude=".DS_Store",
    #     local_dir=DEPLOY_PATH.rstrip('/') + '/',
    #     delete=True,
    #     extra_opts='-c',
    # )
    local("make publish")

def gh_pages():
    """Publish to GitHub Pages"""
    rebuild()
    local("ghp-import -b {github_pages_branch} {deploy_path}".format(**env))
    local("git push origin {github_pages_branch}".format(**env))

def slugify(s):
    s = re.sub(r'[^ A-Za-z_\-0-9]', '', s)
    s = s.lower()
    s = s.replace(' ', '-')
    return s
def fmtdate(d):
    return d.strftime('%Y-%m-%d %H:%M')

PARAMS = ('title', 'slug', 'category', 'tags')
def newpost():
    params = dict(
        (key, raw_input(key.title()+": "))
        for key in PARAMS
    )
    today = datetime.datetime.now()
    if not params['slug']:
        params['slug'] = slugify(params['title'])

    filename = "content/{category}/{year}/{slug}.rst".format(
        year=today.year,
        month=today.month,
        slug=params['slug'],
        category=params['category'],
    )
    f = open(filename, "w")
    with f:
        print >>f, params['title']
        print >>f, "#" * len(params['title'])
        print >>f, ":date:", fmtdate(today)
        for key in params:
            print >>f, ":{}: {}".format(key, params[key])

        # paste = raw_input("Paste contents?")
        # if paste[0].lower() == 'y':
        #     for line in sys.stdin:
        #         print >>f, line
    os.system("atom %s" % (filename,))
