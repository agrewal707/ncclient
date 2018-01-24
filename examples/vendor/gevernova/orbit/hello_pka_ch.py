#! /usr/bin/env python3
#
# Wait for NETCONF call-home connection from Orbit/Orbit-X on the given
# local host address/port, establish connection using public-key based
# authentication and display its capabilities.
#
# $ ./hello_pka_ch.py 192.168.1.7 4334 nms <path-to-id_rsa> <path-to-ssh-config>

import sys, os, warnings
warnings.simplefilter("ignore", DeprecationWarning)
from ncclient import manager
import logging
#logging.basicConfig(level=logging.DEBUG)

def demo(host, port, user, key_filename, ssh_config):
    with manager.call_home(
        host=host,
        port=port,
        username=user,
        key_filename=key_filename,
        allow_agent=False,
        look_for_keys=False,
        hostkey_verify=False,
        ssh_config=ssh_config,
        timeout=180,
        device_params = {'name':'orbit'}) as m:
        for c in m.server_capabilities:
            print(c)

if __name__ == '__main__':
    demo(sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5])
