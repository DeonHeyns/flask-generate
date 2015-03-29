#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'DeonHeyns'


"""
Hook to call flask-generate automatically through virtualenvwrapper_.
when create a new project using the template `base`::
    $ mkproject -t base
.. _virtualenvwrapper: http://virtualenvwrapper.readthedocs.org
"""

import logging
import subprocess

log = logging.getLogger('scaffold')


def template(args):
    project = args[0]
    log.info('Running "flask-generate -p %s"', project)
    subprocess.check_call(['flask-generate', '-p', project, '-d', '..'])