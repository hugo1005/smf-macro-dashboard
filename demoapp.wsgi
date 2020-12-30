import sys
sys.path.insert(0, ‘var/www/html/flaskapp/demoapp’)

print("WSGI File detected")
from demoapp import app as application