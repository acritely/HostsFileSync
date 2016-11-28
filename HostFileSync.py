#
# Host File Sync script
# Sean Hannon 2016
#
# retrieves host file from someonewhocares.org
# writes file to os-specific etc dir
#

import os
import sys
import urllib2
#import getpass

#build path to existing hosts file
local_platform = sys.platform

#switch on os type
if sys.platform.startswith('darwin') :
   host_path = '/private/etc/hosts'

#if sys.platform.startswith('linux') :
# todo windows

#user = getpass.getuser()


url = 'http://someonewhocares.org/hosts/zero/hosts'
open_url = urllib2.urlopen(url)

#write file to hosts path
with open(host_path, 'w') as f:
  #  f.write(local_platform)	
   # f.write(user)
    f.write(open_url.read())