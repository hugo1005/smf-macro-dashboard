#flaskapp.wsgi
import sys
sys.path.insert(0, '/var/www/html/smf-macro-dashboard')

from smf-macro-dashboard import app as application