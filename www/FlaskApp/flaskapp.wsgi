#!/usr/bin/python

import sys
import os
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, os.getcwd())

from FlaskApp import app as application
application.secret_key = 'asdfadfads22340sdfl2ei2'
