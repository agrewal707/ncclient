#! /usr/bin/env python3
#
# Reboot to active version.
#
# $ ./reboot.py 192.168.1.1 admin admin

import sys, os, warnings
warnings.simplefilter("ignore", DeprecationWarning)
from ncclient import manager

import logging
#logging.basicConfig(level=logging.DEBUG)

reboot = """<system-restart xmlns="com:gemds:mds-system"></system-restart>"""

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
        out = m.rpc(reboot)
        print(out)

if __name__ == '__main__':
    demo(sys.argv[1], sys.argv[2], sys.argv[3])
