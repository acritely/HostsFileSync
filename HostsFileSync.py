# -*- coding: utf-8 -*-
#
# Hosts File Sync script
# Sean Hannon 2016
#
# retrieves host file from someonewhocares.org
# writes file to os-specific etc dir
#

import os
import sys
import urllib2

#build path to existing hosts file
local_platform = sys.platform
host_path = ''

print "reading OS..."

#switch on os type
if sys.platform.startswith('darwin') :
   host_path = '/private/etc/hosts'
   
if sys.platform.startswith('win') :
   host_path = 'C:\Windows\System32\drivers\etc\hosts'

if sys.platform.startswith('linux') :
	host_path = '/etc/hosts'
	
if host_path is '' :
	print "Unable to resolve OS"
	print sys.platform
	sys.exit()
else :
	print 'updating: ' + host_path

url = 'http://someonewhocares.org/hosts/zero/hosts'
open_url = urllib2.urlopen(url)

#write file to hosts path
with open(host_path, 'w') as f:
    f.write(open_url.read())

print 'host file updated!'	
