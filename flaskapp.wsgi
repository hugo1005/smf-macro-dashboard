#flaskapp.wsgi

activate_this = '/home/ubuntu/flaskapp/venv/bin/activate_this.py'
with open(activate_this) as f:
	exec(f.read(), dict(__file__=activate_this))

import sys

sys.path.insert(0,"/var/www/html/flaskapp/")

print("Importing flaskapp...")

from flaskapp import app as application
