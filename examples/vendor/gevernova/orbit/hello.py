#! /usr/bin/env python3
#
# Connect to the Orbit/Orbit-X NETCONF server using password based
# authentication and display its capabilities.
#
# $ ./hello.py 172.16.23.10 admin admin

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
        for c in m.server_capabilities:
            print(c)

if __name__ == '__main__':
    demo(sys.argv[1], sys.argv[2], sys.argv[3])
