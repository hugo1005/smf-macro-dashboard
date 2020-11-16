#flaskapp.wsgi
import sys
sys.path.insert(0, '/var/www/html/smf-macro-dashboard')

from flaskapp import app as application