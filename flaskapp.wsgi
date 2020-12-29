#flaskapp.wsgi
import sys
sys.path.insert(0, '/var/www/html/flaskapp/')
activate_this =  './vue_env/bin/activate.py'
execfile(activate_this, dict(__file__=activate_this))

from flaskapp import app as application