# -*- coding: latin-1 -*-

try:
	import PyQt4
        from . forms import Form
except ImportError:
	print "Unable found PyQt4, try install it and run again."