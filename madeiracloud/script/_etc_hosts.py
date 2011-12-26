#!/usr/bin/env python -u
# coding: utf-8

# -------------------------------------------------------------------------- #
# Copyright 2011, MadeiraCloud (support@madeiracloud.com)                  	 #
# -------------------------------------------------------------------------- #
from xml.dom import minidom

def _amazon(mode, ns):
	hosts = [
		"127.0.0.1   localhost localhost.localdomain"
	]
	for hostname in ns:
		hosts.append("%s		%s" % (ns[hostname], hostname))

	f = open("/etc/hosts", "w+")
	f.writelines(hosts)
	f.close()

def _redhat(mode, ns):
	hosts = [
		"127.0.0.1               localhost.localdomain localhost"
	]
	for hostname in ns:
		hosts.append("%s		%s" % (ns[hostname], hostname))

	f = open("/etc/hosts", "w+")
	f.writelines(hosts)
	f.close()

def _centos(mode, ns):
	hosts = [
		"127.0.0.1               localhost.localdomain localhost"
	]
	for hostname in ns:
		hosts.append("%s		%s" % (ns[hostname], hostname))

	f = open("/etc/hosts", "w+")
	f.writelines(hosts)
	f.close()

def _debian(mode, ns):
	hosts = [
		"127.0.0.1 localhost.localdomain localhost"
	]
	for hostname in ns:
		hosts.append("%s		%s" % (ns[hostname], hostname))
	hosts.extend([
		"::1 ip6-localhost ip6-loopback",
		"fe00::0 ip6-localnet",
		"ff00::0 ip6-mcastprefix",
		"ff02::1 ip6-allnodes",
		"ff02::2 ip6-allrouters",
		"ff02::3 ip6-allhosts"
	])

	f = open("/etc/hosts", "w+")
	f.writelines(hosts)
	f.close()

def _ubuntu(mode, ns):
	hosts = [
		"127.0.0.1 localhost"
	]
	for hostname in ns:
		hosts.append("%s		%s" % (ns[hostname], hostname))
	hosts.extend([
		"::1 ip6-localhost ip6-loopback",
		"fe00::0 ip6-localnet",
		"ff00::0 ip6-mcastprefix",
		"ff02::1 ip6-allnodes",
		"ff02::2 ip6-allrouters",
		"ff02::3 ip6-allhosts"
	])

	f = open("/etc/hosts", "w+")
	f.writelines(hosts)
	f.close()

def _suse(mode, ns):
	hosts = [
		"127.0.0.1       localhost"
	]
	for hostname in ns:
		hosts.append("%s		%s" % (ns[hostname], hostname))
	hosts.extend([
		"# special IPv6 addresses",
		"::1             localhost ipv6-localhost ipv6-loopback",
		"fe00::0         ipv6-localnet",
		"ff00::0         ipv6-mcastprefix",
		"ff02::1         ipv6-allnodes",
		"ff02::2         ipv6-allrouters",
		"ff02::3         ipv6-allhosts"
	])

	f = open("/etc/hosts", "w+")
	f.writelines(hosts)
	f.close()

Distro = {
	'amazon'	:	_amazon,
	'redhat'	:	_redhat,
	'centOS'	:	_centos,
	'debian'	:	_debian,
	'ubuntu'	:	_ubuntu,
	'suse'		:	_suse
}

def do(self, params, distro):
	ns = {}
	mode = 'Insert'

	try:
		# params
		doc = minidom.parseString(params)
		doc.getElementsByTagName('item')
		params = doc.getElementsByTagName('params')
		if not params:
			logging.error("Missing parameters")
			raise Exception
		if len(params) > 1:
			loggging.warning("Multiple parameters, will use the first one only")
		items = params[0].getElementsByTagName('item')
		if not items:
			logging.error("Missing parameters")
			raise Exception
		for i in items:
			if i.attributes.has_key('mode'):
				mode = i.attributes['mode'].firstChild.data
				continue
			if i.attributes.has_key('hostname') and i.attributes.has_key('ip'):
				ns[i.attributes['hostname'].firstChild.data] = i.attributes['ip'].firstChild.data
				continue
		if not ns:
			logging.error("Invalid parameters")
			raise Exception
		if mode not in ('Insert', 'Overwrite', 'Append'):	
			logging.warning("Invalid script mode: %s, will use Insert by default" % mode)
			mode = 'Overwrite'									# Insert, Overwrite, Append

		# check distro
		return Distro[distro](mode, ns)
	except:
		return None

