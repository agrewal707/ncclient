#! /usr/bin/env python3
#
# Retrieve the running config from the NETCONF server passed on the
# command line using get-config and write the XML configs to files.
#
# $ ./verify_image.py 192.168.1.1 admin admin

import sys, os, warnings
warnings.simplefilter("ignore", DeprecationWarning)
from ncclient import manager

import logging
#logging.basicConfig(level=logging.DEBUG)

verify_image_1 = """<verify-image xmlns="com:gemds:mds-system"><location>1</location></verify-image>"""

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
        out = m.rpc(verify_image_1)
        print(out)

if __name__ == '__main__':
    demo(sys.argv[1], sys.argv[2], sys.argv[3])
