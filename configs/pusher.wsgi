activate_this = '/var/www/pusher/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
import sys
path = ['/var/www/pusher/lib/python2.7/site-packages', '/var/www/', '/var/www/pusher']
for p in path:
	if p not in sys.path:
		sys.path.append(p)
#if '/var/www/pusher/lib/python2.7/site-packages' in sys.path:
#	sys.path.append('/var/www/pusher/lib/python2.7/site-packages')
#sys.path.insert(0, '/var/www/pusher/lib/python2.7/site-packages')
#sys.path.insert(0, '/var/www/pusher')
#sys.stderr.write(",".join(sys.path))
from Pusher import app as application
