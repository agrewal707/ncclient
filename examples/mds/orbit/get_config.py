#! /usr/bin/env python2.7
#
# Retrieve the running config from the NETCONF server passed on the
# command line using get-config and write the XML configs to files.
#
# $ ./get_config.py 192.168.1.1 admin admin

import sys, os, warnings
warnings.simplefilter("ignore", DeprecationWarning)
from ncclient import manager

import logging
#logging.basicConfig(level=logging.DEBUG)


def demo(host, user, passwd):
     with manager.connect(
        host=host,
        port=830,
        username=user,
        password=passwd,
        allow_agent=False,
        look_for_keys=False,
        hostkey_verify=False,
        device_params = {'name':'orbit'}) as m:
        c = m.get_config(source='running').data_xml
        with open("%s.xml" % host, 'w') as f:
            f.write(c)

if __name__ == '__main__':
    demo(sys.argv[1], sys.argv[2], sys.argv[3])
