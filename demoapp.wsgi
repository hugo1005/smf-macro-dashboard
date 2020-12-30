import sys

activate_this = '/home/ubuntu/flaskapp/venv/bin/activate_this.py'
with open(activate_this) as f:
	exec(f.read(), dict(__file__=activate_this))

sys.path.insert(0,"var/www/html/flaskapp")

print("WSGI File detected")
from demoapp import app as application