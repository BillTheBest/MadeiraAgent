#!/usr/bin/env python -u
# coding: utf-8

# -------------------------------------------------------------------------- #
# Copyright (c) 20011 MadeiraCloud, All Rights Reserved.
#
# License
# -------------------------------------------------------------------------- #
import os
import sys
import platform
from setuptools import setup, find_packages

from madeiracloud import __copyright__ 	
from madeiracloud import __license__ 		
from madeiracloud import __version__ 		
from madeiracloud import __maintainer__ 	
from madeiracloud import __author__ 		
from madeiracloud import __email__ 		
from madeiracloud import __status__ 		
from madeiracloud import __url__ 		
from madeiracloud import __classifier__

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

def rread(*rnames):
	return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

# check user
if os.getuid() != 0:
	print >> sys.stderr, 'Please use root to install this package\n'
	sys.exit(1)

# check Python's version
if sys.version_info < (2, 6):
	print >> sys.stderr, 'Please use Python 2.6 or later\n'
	sys.exit(1)

# check OS
if platform.system() != 'Linux':
	print >> sys.stderr, 'This package is for Linux only'
	sys.exit(1)

# check Distro
distro=platform.linux_distribution()

# check Arch
#arch = platform.machine()
#
#long_description = ("""
#%s
#
#%s
#-----------------------------------------------------------------------
#%s
#""" % (readme, chaneglog, license))

setup(
	name 			= "MadeiraCloud",
	version			= __version__,
	url 			= __url__,
	author 			= __author__,
	author_email 	= __email__,
	license 		= __license__,
	keywords 		= "MadeiraCloud AWS",
	description 	= ("MadeiraCloud Agent"),	
	#long_description= read('README'),
	classifiers		= __classifier__,
	packages		= ['madeiracloud', 'madeiracloud.script'],
	scripts			= ['bin/madeira.py'],
	install_requires = ['pyinotify'],
	include_package_datan= True,	
)

if sys.argv[-1] == 'install':
	os.system('sh %s/script/%s.sh' % (os.path.dirname(os.path.abspath(__file__)), distro[0].lower()))
	
	print >> sys.stdout, """
Finished! MadeiraCloud has been installed on this machine.

The package is located at /usr/share/madeiracloud
To start, stop and restart the program, use /etc/init.d/madeiracloud 

Please visit www.madeiracloud.com for more

---------- Enjoy! ----------
    The MadeiraCloud Team
"""
