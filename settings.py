import os

# configuration
DEBUG = 'RSTED_PROD' not in os.environ

RUN_PATH = 'var/run'
PID_FILE = 'fastcgi.pid'
SOCKET_FILE = 'rsted.sock'
FCGI_UMASK = '000' # you can override this in settings_local.py if you wish

HOST = "0.0.0.0"  ## Listen IP
                  ## 0.0.0.0   is open to everyone,
                  ## 127.0.0.1 is localhost only.
PORT = 5001


try:
    from settings_local import *
except ImportError:
    pass
