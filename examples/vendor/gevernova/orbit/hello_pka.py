#! /usr/bin/env python3
#
# Connect to the Orbit/Orbit-X NETCONF server using public-key based
# authentication and display its capabilities.
#
# $ ./hello_pka.py 192.168.1.1 nms <path-to-id_rsa> <path-to-ssh-config>

import sys, os, warnings
warnings.simplefilter("ignore", DeprecationWarning)
from ncclient import manager
import logging
#logging.basicConfig(level=logging.DEBUG)

def demo(host, user, key_filename, ssh_config):
    with manager.connect(
        host=host,
        port=830,
        username=user,
        key_filename=key_filename,
        allow_agent=False,
        look_for_keys=False,
        hostkey_verify=False,
        ssh_config=ssh_config,
        device_params = {'name':'orbit'}) as m:
        for c in m.server_capabilities:
            print(c)

if __name__ == '__main__':
    demo(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
