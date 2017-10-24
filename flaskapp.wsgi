#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")
sys.path.append('/usr/lib/python2.7')
sys.path.append('/usr/lib/python2.7/plat-x86_64-linux-gnu')
sys.path.append('/usr/lib/python2.7/lib-tk')
sys.path.append('/usr/lib/python2.7/lib-old')
sys.path.append('/usr/lib/python2.7/lib-dynload')
sys.path.append('/usr/local/lib/python2.7/dist-packages')
sys.path.append('/usr/lib/python2.7/dist-packages')

from FlaskApp import app as application
application.secret_key = 'bkuzfkutd'
