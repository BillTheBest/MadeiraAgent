#!/usr/bin/env python -u

# -------------------------------------------------------------------------- #
# Copyright 2011, MadeiraCloud (support@madeiracloud.com)                  	 #
# -------------------------------------------------------------------------- #
import logging
from xml.dom import minidom

import script

Script = {
	'/etc/hosts'	:	script._etc_hosts
}

# E_OK, (timestamp, [{k:[]}])
# [
# 	{
# 		'code': ['/etc/hosts'], 
# 		'params': ['<?xml version="1.0" ?>\n<instant>\n\t<task>\n\t\t<params>\n\t\t\t<item mode=\'Insert, Overwrite, Append\'></item>\n\t\t\t<item hostname=\'async\' ip=\'211.98.26.9\'></item>\n\\t\t<item hostname=\'test\' ip=\'211.98.26.8\'></item>\t\n\t\t</params>\n\t</task>\n</instant>\n'], 
# 		'id': ['12345678']
# 	}
# ]
def run(endpoint, instance_id, distro):
	res = {}

	try:
		# get
		server = Server(endpoint)
		(err, data) = server.fetch(instance_id)
		if err:		raise Exception("Failed to get new task")
		tasks = data[1]

		if not tasks:
			logging.info("No pending task")
			return

		# execute
		for t in tasks:
			if not Script.has_key(t['code'][0]):
				logging.error("Invalid task code: %s" % t['code'][0])
	
			res[t['id'][0]] = Script[t['code'][0]].do(t['params'][0], distro)	# (0, data)
			if res[t['id'][0]] is not None:
				logging.info("Successfully executed script %s with parameters %s" % (task['code'][0], task['params'][0]))

		# report
		(err, data) = server.report(res)
	except Exception, e:
		logging.error("Error during executing pending task: %s" % e)
